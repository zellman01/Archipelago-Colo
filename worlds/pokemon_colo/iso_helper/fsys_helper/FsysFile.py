from io import BytesIO

from .FsysFileDetail import FileType, FsysFileDetail
from .FsysFileEntry import FsysFileEntry

class FsysFile:
    fsys_file_size_offset = 0x20
    number_of_file_entries_offset = 0x0C
    first_file_details_pointer_offset = 0x60

    #File Details
    file_id_offset = 0x00
    file_format_offset = 0x02
    file_start_pointer_offset = 0x04
    uncompressed_size_offset = 0x08
    compressed_size_offset = 0x14
    file_format_index_offset = 0x20
    file_name_offset = 0x24

    def __init__(self, filename, stream: BytesIO):
        self.filename = filename
        self.stream = stream
        self.file_entries = []

        for i in range(self.__number_of_entries()):
            start = self.__get_int_at_offset(self.first_file_details_pointer_offset + i * 4)
            nameOffset = self.__get_uint_at_offset(start + self.file_name_offset)
            file_details = FsysFileDetail(
                id=self.__get_ushort_at_offset(start),
                filetype=FileType(self.__get_byte_at_offset(start + self.file_format_offset)),
                start_offset=self.__get_uint_at_offset(start + self.file_start_pointer_offset),
                uncompressed_size=self.__get_uint_at_offset(start + self.uncompressed_size_offset),
                compressed_size=self.__get_uint_at_offset(start + self.compressed_size_offset),
                file_format_index=self.__get_uint_at_offset(start + self.file_format_index_offset),
                name_offset=nameOffset,
                filename=self.__get_fst_string_at_offset(nameOffset)
            )
            self.file_entries.append(FsysFileEntry.extract_from_fsys(self.stream, file_details))

    def get_entry_by_filename(self, filename: str, filetype: FileType) -> FsysFileEntry:
        for entry in self.file_entries:
            if entry.file_detail.filename == filename and entry.file_detail.filetype == filetype:
                return entry
        raise Exception(f"File with name '{filename}' not found in fsys '{self.filename}'")

    def save(self) -> BytesIO:
        self.stream.seek(self.first_file_details_pointer_offset)
        self.stream.truncate(self.stream.tell())

        size_of_detail_pointers = len(self.file_entries) * 4
        alignment_check = size_of_detail_pointers % 16
        alignment = 0
        if alignment_check != 0:
            alignment = 16 - alignment_check

        start_name_offset = self.first_file_details_pointer_offset + size_of_detail_pointers + alignment
        self.stream.seek(start_name_offset)

        # Write file names
        start_date_offset = -1
        for entry in self.file_entries:
            self.stream.write(entry.file_detail.filename.encode('utf-8'))
            self.stream.write(b'\x00')

            if entry.file_detail.start_offset < start_date_offset:
                start_date_offset = entry.file_detail.start_offset

        self.__align_stream(self.stream, 0x10)
  
        detail_headers_start_offset = int(self.stream.tell())

        # write pointers to detail headers offset
        self.stream.seek(self.first_file_details_pointer_offset)
        for x in range(len(self.file_entries)):
            self.stream.write((detail_headers_start_offset + (x * 0x50)).to_bytes(4, byteorder='big'))

        last_detail_header_end_offset = detail_headers_start_offset + (len(self.file_entries) * 0x50)
        self.stream.seek(last_detail_header_end_offset)
        self.__align_stream(self.stream, 0x10)

        first_file_start_offset = self.stream.tell()
        self.file_entries[0].file_detail.start_offset = first_file_start_offset

        # write detail headers and entries
        for i in range(len(self.file_entries)):
            entry = self.file_entries[i]
            detail_header = entry.file_detail

            data = entry.data
            length = len(data)
            encoded_data = entry.raw_data
            encoded_length = len(encoded_data)

            self.stream.seek(detail_header.start_offset)
            self.stream.write(encoded_data)

            detail_header.uncompressed_size = length

            if encoded_length != detail_header.compressed_size:
                 adjusted_size = encoded_length - detail_header.compressed_size
                 detail_header.compressed_size = encoded_length

                # adjust offsets of future files
                 for j in range(i + 1, len(self.file_entries)):
                    adj_details_header = self.file_entries[j].file_detail
                    adj_details_header.start_offset += adjusted_size

                    alignment_check = adj_details_header.start_offset % 0x10
                    alignment = 0
                    if alignment_check != 0:
                        alignment = 0x10 - alignment_check
                    adj_details_header.start_offset += alignment
        
        self.__align_stream(self.stream, 0x10)
        self.stream.write(b'\x10')
        self.stream.seek(-4, 1)
        self.stream.write(bytearray([0x46, 0x53, 0x59, 0x53]))

        self.stream.seek(0, 2)
        length = self.stream.tell()

        self.stream.seek(self.fsys_file_size_offset)
        self.stream.write(length.to_bytes(4, byteorder='big'))

        self.stream.seek(detail_headers_start_offset)
        for entry in self.file_entries:
            detail_header = entry.file_detail
            self.stream.write(detail_header.id.to_bytes(2, byteorder='big'))
            self.stream.write(detail_header.filetype.value.to_bytes(1, byteorder='big'))
            self.stream.write((0).to_bytes(1, byteorder='big')) # padding
            self.stream.write(detail_header.start_offset.to_bytes(4, byteorder='big'))
            self.stream.write(detail_header.uncompressed_size.to_bytes(4, byteorder='big'))
            self.stream.write(bytearray([0x80, 0, 0, 0])) # Mystery Bytes
            self.stream.write(bytearray([0x00] * 4)) # padding
            self.stream.write(detail_header.compressed_size.to_bytes(4, byteorder='big'))
            self.stream.write(bytearray([0x00] * 8)) # padding
            self.stream.write(detail_header.file_format_index.to_bytes(4, byteorder='big'))
            self.stream.write(detail_header.name_offset.to_bytes(4, byteorder='big'))
            self.stream.write(bytearray([0x00] * 12)) # padding
            self.stream.write(bytearray([0x11] * 12)) # padding

        self.stream.seek(0)
        return self.stream
        

    def __number_of_entries(self):
        return self.__get_uint_at_offset(self.number_of_file_entries_offset)
    
    def __get_uint_at_offset(self, offset):
        self.stream.seek(offset)
        return int.from_bytes(self.stream.read(4), byteorder='big')
    
    def __get_int_at_offset(self, offset):
        self.stream.seek(offset)
        return int.from_bytes(self.stream.read(4), byteorder='big', signed=True)
    
    def __get_ushort_at_offset(self, offset):
        self.stream.seek(offset)
        return int.from_bytes(self.stream.read(2), byteorder='big')
    
    def __get_byte_at_offset(self, offset):
        self.stream.seek(offset)
        return int.from_bytes(self.stream.read(1), byteorder='big')
    
    def __get_fst_string_at_offset(self, offset):
        self.stream.seek(offset)
        string_bytes = bytearray()
        while True:
            byte = self.stream.read(1)
            if byte == b'\x00':
                break
            string_bytes.extend(byte)
        return string_bytes.decode('utf-8')
    
    def __align_stream(self, stream: BytesIO, alignment):
        current_pos = stream.tell()

        stream.seek(0, 2)
        length = stream.tell()

        alignment_check = length % alignment
        if alignment_check != 0:
            padding_needed = alignment - alignment_check
            stream.write(b'\x00' * padding_needed)

        stream.seek(current_pos)