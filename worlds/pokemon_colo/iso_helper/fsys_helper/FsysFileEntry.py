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
    def __init__(self, filetype: FileType, data: bytearray, file_detail: FsysFileDetail):
        self.filetype = filetype
        self.data = data
        self.file_detail = file_detail

    def encode(self) -> BytesIO:
        if self.file_detail.file_is_compressed():
            encoder = LzssEncoder()
            encoded = encoder.encode(self.data)
            stream = BytesIO(encoded)
        else:
            stream = BytesIO(self.data)
        
        return stream

    @staticmethod
    def extract_from_fsys(fsys_stream: BytesIO, file_detail: FsysFileDetail) -> "FsysFileEntry":
        fsys_stream.seek(file_detail.start_offset)
        size = file_detail.compressed_size if file_detail.file_is_compressed() else file_detail.uncompressed_size
        raw_data = fsys_stream.read(size)

        if file_detail.file_is_compressed():
            data = bytearray(LzssEncoder.decode(raw_data[SIZE_OF_LZSS_HEADER:]))
        else:
            data = bytearray(raw_data)

        return FsysFileEntry.create_extracted_file(file_detail.filetype, data, file_detail)

    @staticmethod
    def create_extracted_file(filetype: FileType, data: bytearray, file_detail: FsysFileDetail) -> "FsysFileEntry":
        if filetype in (FileType.GTX, FileType.ATX):
            return Texture(filetype, data, file_detail)
        elif filetype == FileType.GSW:
            return GSWTexture(data, file_detail)
        elif filetype == FileType.PKX:
            return PKX(data, file_detail)
        elif filetype == FileType.MSG:
            return StringTable(data, file_detail)
        elif filetype == FileType.REL:
            return REL(data, file_detail)
        elif filetype == FileType.SCD:
            return SCD(data, file_detail)
        else:
            return FsysFileEntry(filetype, data, file_detail)


class Texture(FsysFileEntry):
    def __init__(self, filetype: FileType, data: bytearray, file_detail: FsysFileDetail):
        super().__init__(filetype, data, file_detail)


class GSWTexture(FsysFileEntry):
    def __init__(self, data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.GSW, data, file_detail)


class PKX(FsysFileEntry):
    def __init__(self, data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.PKX, data, file_detail)


class StringTable(FsysFileEntry):
    def __init__(self, data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.MSG, data, file_detail)


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
    
    def __init__(self, data: bytearray, file_detail: FsysFileDetail):
        if file_detail.filename.find("common_rel") != -1:
            self.data_start_offset = DataReadHelper.int_from_bytes(data, self.common_rel_data_start_offset_location)
        else:
            self.data_start_offset = DataReadHelper.int_from_bytes(data, self.rel_data_start_offset_location)

        self.pointer_start_offset = DataReadHelper.int_from_bytes(data, self.rel_pointers_start_offset_location)
        self.first_pointer_offset = self.pointer_start_offset + self.rel_pointers_first_pointer_offset

        pointer_header_offset = DataReadHelper.int_from_bytes(data, self.rel_pointers_header_pointer1_offset, signed=True)
        pointer_end_offset = DataReadHelper.int_from_bytes(data, pointer_header_offset + 0xC, signed=True)
        self.number_of_pointers = 0
        current_offset = self.first_pointer_offset
        end = False

        while current_offset < pointer_end_offset and not end:
            val = DataReadHelper.int_from_bytes(data, current_offset, True)
            end = val >= 0xCA01 and val <= 0xCAFF
            if not end:
                self.number_of_pointers += 1
            current_offset += self.rel_size_of_pointer

        super().__init__(FileType.REL, data, file_detail)


class SCD(FsysFileEntry):
    def __init__(self, data: bytearray, file_detail: FsysFileDetail):
        super().__init__(FileType.SCD, data, file_detail)
