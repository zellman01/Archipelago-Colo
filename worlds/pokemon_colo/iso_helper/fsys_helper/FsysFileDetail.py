from enum import Enum

class FileType(Enum):
    NaN = 0x00
    RDAT = 0x02  # room model in hal dat format (unknown if it uses a different file extension)
    DAT = 0x04  # character model in hal dat format
    CCD = 0x06  # collision file
    SAMP = 0x08  # shorter music files for fanfares etc.
    MSG = 0x0a  # string table
    FNT = 0x0c  # font
    SCD = 0x0e  # script data
    DATS = 0x10  # multiple .dat models in one archive
    GTX = 0x12  # texture
    GPT1 = 0x14  # particle data
    CAM = 0x18  # camera data
    REL = 0x1c  # relocation table
    PKX = 0x1e  # character battle model (same as dat with additional header information)
    WZX = 0x20  # move animation
    UNKNOWN = 0x22 # TODO what is this filetype?
    UNKNOWN2 = 0x26 # TODO what is this filetype?
    ISD = 0x28  # audio file header
    ISH = 0x2a  # audio file
    THH = 0x2c  # thp media header
    THD = 0x2e  # thp media data
    GSW = 0x30  # multi texture
    ATX = 0x32  # animated texture (official file extension is currently unknown)
    BIN = 0x34  # binary data

class FsysFileDetail:
    def __init__(self, id, filetype, start_offset, uncompressed_size, compressed_size, file_format_index, name_offset, filename):
        self.id = id
        self.filetype = filetype
        self.start_offset = start_offset
        self.uncompressed_size = uncompressed_size
        self.compressed_size = compressed_size
        self.file_format_index = file_format_index
        self.name_offset = name_offset
        self.filename = filename

    def file_is_compressed(self):
        return self.compressed_size != self.uncompressed_size        