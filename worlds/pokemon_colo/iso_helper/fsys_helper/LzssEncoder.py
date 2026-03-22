import io
import struct

EI = 12           # offset bits
EJ = 4            # length bits
P = 2             # threshold
UNCODED_F = 1 << EJ   # 16
ENCODED_F = 18

N = 1 << EI       # window size = 4096
LZSS_BYTES = 0x4C5A5353
LZSS_UNCOMPRESSED_SIZE_OFFSET = 0x04
LZSS_COMPRESSED_SIZE_OFFSET = 0x08
LZSS_UNKNOWN_OFFSET = 0x0C  # PBR only, unused in Colo/XD


class LzssEncoder:

    def __init__(self):
        self.lson = [0] * (N + 1)
        self.rson = [0] * (N + 257)
        self.dad = [0] * (N + 1)
        self.match_length = 0
        self.match_value = 0

    def _init_tree(self):
        for i in range(N + 1, N + 257):
            self.rson[i] = N
        for i in range(N):
            self.dad[i] = N

    def _insert_node(self, r: int, sliding_window: bytearray):
        cmp = 1
        key = r
        p = N + 1 + sliding_window[key]
        self.rson[r] = self.lson[r] = N
        self.match_length = 0
        while True:
            if cmp >= 0:
                if self.rson[p] != N:
                    p = self.rson[p]
                else:
                    self.rson[p] = r
                    self.dad[r] = p
                    return
            else:
                if self.lson[p] != N:
                    p = self.lson[p]
                else:
                    self.lson[p] = r
                    self.dad[r] = p
                    return
            cmp = 0
            for i in range(1, ENCODED_F):
                cmp = sliding_window[key + i] - sliding_window[p + i]
                if cmp != 0:
                    break
            else:
                i = ENCODED_F
            if i > self.match_length:
                self.match_value = p
                self.match_length = i
                if self.match_length >= ENCODED_F:
                    break
        self.dad[r] = self.dad[p]
        self.lson[r] = self.lson[p]
        self.rson[r] = self.rson[p]
        self.dad[self.lson[p]] = r
        self.dad[self.rson[p]] = r
        if self.rson[self.dad[p]] == p:
            self.rson[self.dad[p]] = r
        else:
            self.lson[self.dad[p]] = r
        self.dad[p] = N  # remove p

    def _delete_node(self, p: int):
        if self.dad[p] == N:
            return  # not in tree
        if self.rson[p] == N:
            q = self.lson[p]
        elif self.lson[p] == N:
            q = self.rson[p]
        else:
            q = self.lson[p]
            if self.rson[q] != N:
                while self.rson[q] != N:
                    q = self.rson[q]
                self.rson[self.dad[q]] = self.lson[q]
                self.dad[self.lson[q]] = self.dad[q]
                self.lson[q] = self.lson[p]
                self.dad[self.lson[p]] = q
            self.rson[q] = self.rson[p]
            self.dad[self.rson[p]] = q
        self.dad[q] = self.dad[p]
        if self.rson[self.dad[p]] == p:
            self.rson[self.dad[p]] = q
        else:
            self.lson[self.dad[p]] = q
        self.dad[p] = N

    def encode(self, data: bytes) -> bytes:
        file = io.BytesIO(data)
        file_len = len(data)

        output = io.BytesIO()
        # Write header
        output.write(struct.pack(">I", LZSS_BYTES))
        output.write(struct.pack(">i", file_len))
        output.write(struct.pack(">i", 0))  # compressed size placeholder
        output.write(struct.pack(">i", 0))  # unknown

        sliding_window = bytearray(N + ENCODED_F - 1)
        self.lson = [0] * (N + 1)
        self.rson = [0] * (N + 257)
        self.dad = [0] * (N + 1)

        self._init_tree()

        code_buf = bytearray(17)
        code_buf[0] = 0
        code_buf_ptr = 1
        mask = 1
        codesize = 0

        s = 0
        r = N - ENCODED_F

        # clear buffer
        for i in range(s, r):
            sliding_window[i] = 0

        length = 0
        while length < ENCODED_F:
            c = file.read(1)
            if not c:
                break
            sliding_window[r + length] = c[0]
            length += 1

        if length == 0:
            # empty input — return header only with 0 compressed size
            return output.getvalue()

        for i in range(1, ENCODED_F + 1):
            self._insert_node(r - i, sliding_window)
        self._insert_node(r, sliding_window)

        while length > 0:
            if self.match_length > length:
                self.match_length = length

            if self.match_length <= P:
                self.match_length = 1
                code_buf[0] |= mask
                code_buf[code_buf_ptr] = sliding_window[r]
                code_buf_ptr += 1
            else:
                code_buf[code_buf_ptr] = self.match_value & 0xFF
                code_buf_ptr += 1
                code_buf[code_buf_ptr] = (
                    ((self.match_value >> 4) & 0xF0)
                    | (self.match_length - (P + 1))
                ) & 0xFF
                code_buf_ptr += 1

            mask = (mask << 1) & 0xFF
            if mask == 0:
                for i in range(code_buf_ptr):
                    output.write(bytes([code_buf[i]]))
                codesize += code_buf_ptr
                code_buf = bytearray(17)
                code_buf_ptr = 1
                mask = 1

            last_match_length = self.match_length
            i = 0
            while i < last_match_length:
                c = file.read(1)
                if not c:
                    break
                self._delete_node(s)
                sliding_window[s] = c[0]
                if s < ENCODED_F - 1:
                    sliding_window[s + N] = c[0]
                s = (s + 1) & (N - 1)
                r = (r + 1) & (N - 1)
                self._insert_node(r, sliding_window)
                i += 1

            while i < last_match_length:
                self._delete_node(s)
                s = (s + 1) & (N - 1)
                r = (r + 1) & (N - 1)
                length -= 1
                if length != 0:
                    self._insert_node(r, sliding_window)
                i += 1

        if code_buf_ptr > 1:
            for i in range(code_buf_ptr):
                output.write(bytes([code_buf[i]]))
            codesize += code_buf_ptr

        # patch compressed size in header
        result = bytearray(output.getvalue())
        struct.pack_into(">i", result, LZSS_COMPRESSED_SIZE_OFFSET, codesize + 0x10)
        return bytes(result)

    @staticmethod
    def decode(data: bytes) -> bytes:
        flags = 0
        n = N
        f = UNCODED_F
        r_less = P

        sliding_window = bytearray(n)
        output = io.BytesIO()

        r = (n - f) - r_less
        n -= 1
        f -= 1

        stream = io.BytesIO(data)

        while True:
            flags >>= 1
            if (flags & 0x100) == 0:
                b = stream.read(1)
                if not b:
                    break
                flags = b[0] | 0xFF00

            if (flags & 0x1) != 0:
                b = stream.read(1)
                if not b:
                    break
                output.write(b)
                sliding_window[r] = b[0]
                r = (r + 1) & n
            else:
                raw_i = stream.read(1)
                if not raw_i:
                    break
                raw_j = stream.read(1)
                if not raw_j:
                    break
                i = raw_i[0]
                j = raw_j[0]
                i |= (j >> EJ) << 8
                j = (j & f) + P
                for k in range(j + 1):
                    b = sliding_window[(i + k) & n]
                    output.write(bytes([b]))
                    sliding_window[r] = b
                    r = (r + 1) & n

        return output.getvalue()
