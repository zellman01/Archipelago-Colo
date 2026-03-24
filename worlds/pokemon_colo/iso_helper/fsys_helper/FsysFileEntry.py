from io import BytesIO
from .LzssEncoder import LzssEncoder
from .FsysFileDetail import FileType, FsysFileDetail

SIZE_OF_LZSS_HEADER = 0x10

class DataReadHelper:
    @staticmethod
    def int_from_bytes(data: bytearray, offset: int, length: int = 4, signed=False) -> int:
        return int.from_bytes(data[offset:offset+length], byteorder='big', signed=signed)
    
    @staticmethod
    def write_int_to_bytes(data: bytearray, offset: int, value: int, length: int = 4, signed=False) -> None:
        data[offset:offset+length] = value.to_bytes(length, byteorder='big', signed=signed)
    

class FsysFileEntry:
    def __init__(self, filetype: FileType, raw_data: bytearray, file_detail: FsysFileDetail):
        self.filetype = filetype
        self.raw_data = raw_data
        self.data = bytearray([])
        self.file_detail = file_detail

    def replace_data(self, new_data: bytearray):
        self.data = new_data
        self.encode()

    def decode(self) -> None:
        if self.file_detail.file_is_compressed():
           self.data = bytearray(LzssEncoder.decode(self.raw_data[SIZE_OF_LZSS_HEADER:]))
        else:
            self.data = bytearray(self.raw_data)

    def encode(self) -> None:
        if self.file_detail.file_is_compressed():
            encoder = LzssEncoder()
            self.raw_data = bytearray(encoder.encode(self.data))
        else:
            self.raw_data = self.data

    @staticmethod
    def extract_from_fsys(fsys_stream: BytesIO, file_detail: FsysFileDetail) -> "FsysFileEntry":
        fsys_stream.seek(file_detail.start_offset)
        size = file_detail.compressed_size if file_detail.file_is_compressed() else file_detail.uncompressed_size
        raw_data = bytearray(fsys_stream.read(size))

        if len(raw_data) != size:
            raise Exception(f"Expected to read {size} bytes for file '{file_detail.filename}' but only read {len(raw_data)} bytes.")

        return FsysFileEntry.create_extracted_file(file_detail.filetype, bytearray(raw_data), file_detail)

    @staticmethod
    def create_extracted_file(filetype: FileType, raw_data: bytearray, file_detail: FsysFileDetail) -> "FsysFileEntry":
        if filetype in (FileType.GTX, FileType.ATX):
            return Texture(filetype, raw_data, file_detail)
        elif filetype == FileType.GSW:
            return GSWTexture(raw_data, file_detail)
        elif filetype == FileType.PKX:
            return PKX(raw_data, file_detail)
        elif filetype == FileType.MSG:
            return StringTable(raw_data, file_detail)
        elif filetype == FileType.REL:
            return REL(raw_data, file_detail)
        elif filetype == FileType.SCD:
            return SCD(raw_data, file_detail)
        else:
            return FsysFileEntry(filetype, raw_data, file_detail)


class Texture(FsysFileEntry):
    def __init__(self, filetype: FileType, raw_data: bytearray, file_detail: FsysFileDetail):
        super().__init__(filetype, raw_data, file_detail)


class GSWTexture(FsysFileEntry):
    def __init__(self, raw_data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.GSW, raw_data, file_detail)


class PKX(FsysFileEntry):
    def __init__(self, raw_data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.PKX, raw_data, file_detail)


class StringTable(FsysFileEntry):
    def __init__(self, raw_data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.MSG, raw_data, file_detail)


class REL(FsysFileEntry):
    common_rel_data_start_offset_location = 0x6c
    rel_data_start_offset_location = 0x64

    rel_pointers_start_offset_location = 0x24
    rel_pointers_header_pointer1_offset = 0x28
    rel_pointers_first_pointer_offset = 0x8
    rel_pointers_data_pointer1_offset = 0x4
    rel_size_of_pointer = 0x10

    def get_pointer_offset(self, index) -> int:
        return int(self.first_pointer_offset + (index * self.rel_size_of_pointer) + self.rel_pointers_data_pointer1_offset)

    def get_pointer(self, index) -> int:
        offset = self.get_pointer_offset(index)
        return DataReadHelper.int_from_bytes(self.data, offset) + self.data_start_offset
    
    def decode(self) -> None:
        super().decode()

        if self.file_detail.filename.find("common_rel") != -1:
            self.data_start_offset = DataReadHelper.int_from_bytes(self.data, self.common_rel_data_start_offset_location)
        else:
            self.data_start_offset = DataReadHelper.int_from_bytes(self.data, self.rel_data_start_offset_location)

        self.pointer_start_offset = DataReadHelper.int_from_bytes(self.data, self.rel_pointers_start_offset_location)
        self.first_pointer_offset = self.pointer_start_offset + self.rel_pointers_first_pointer_offset

        pointer_header_offset = DataReadHelper.int_from_bytes(self.data, self.rel_pointers_header_pointer1_offset, signed=True)
        pointer_end_offset = DataReadHelper.int_from_bytes(self.data, pointer_header_offset + 0xC, signed=True)
        self.number_of_pointers = 0
        current_offset = self.first_pointer_offset
        end = False

        while current_offset < pointer_end_offset and not end:
            val = DataReadHelper.int_from_bytes(self.data, current_offset, True)
            end = val >= 0xCA01 and val <= 0xCAFF
            if not end:
                self.number_of_pointers += 1
            current_offset += self.rel_size_of_pointer


    def __init__(self, raw_data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.REL, raw_data, file_detail)


class SCD(FsysFileEntry):
    def __init__(self, raw_data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.SCD, raw_data, file_detail)
