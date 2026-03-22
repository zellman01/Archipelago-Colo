from io import BytesIO

from .FsysFileDetail import FileType, FsysFileDetail
from .FsysFileEntry import FsysFileEntry

class FsysFile:
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

    file_entries: list[FsysFileEntry] = []

    def __init__(self, filename, stream: BytesIO):
        self.filename = filename
        self.stream = stream

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

    def encode_and_write_to_stream(self):
        for entry in self.file_entries:
            encoded_stream = entry.encode()
            self.stream.seek(entry.file_detail.start_offset)
            self.stream.write(encoded_stream.read())
        

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