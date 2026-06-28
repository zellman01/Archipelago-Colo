from typing import NamedTuple, Optional
from enum import Enum

class PCLocType(Enum):
    NONE = -1
    START = 0
    TRAINER = 1
    SHADOW = 2
    CHEST = 3
    ITEM = 4
    EVENT = 5
    REMATCH = 6
    LAB_FIGHT = 7

class PCItemType(Enum):
    NONE = -1
    POKEMON = 0
    KEYITEM = 1
    ITEM = 2
    POKEBALL = 3
    BERRY = 4 
    TM = 5

class Nature:
    stats = ["Atk", "Def", "Sp. Atk", "Sp. Def", "Spd"]
    def __init__(self, stat1: int, stat2: int, gender: int):
        """
        Creates a Nature object for pokemon created for the player

        Paramerers
        -------
        stat1: The stat to decrease, represented as an int (0 = Atk, 1 = Def, 2 = Sp. Atk, 3 = Sp. Def, 4 = Spd)

        stat2: Same as stat1, but to be increased

        gender: What gender the pokemon is (0 = female, 1 = male)
        """
        self.dec = stat1
        self.inc = stat2
        self.gender = gender

    def nature_hex(self) -> int:
        grid = [[
                [0x0014001E, 0x000B001E, 0x0012001E, 0x0009001E, 0x0002001E],
                [0x0019001E, 0x0010001E, 0x0017001E, 0x000E001E, 0x0007001E],
                [0x000A001E, 0x0001001E, 0x0008001E, 0x0018001E, 0x0011001E],
                [0x000F001E, 0x001F001E, 0x0006001E, 0x0004001E, 0x0016001E],
                [0x0005001E, 0x0015001E, 0x0003001E, 0x0013001E, 0x000C001E]
                ],
                [
                [0x0004001F, 0x0014001F, 0x0002001F, 0x0012001F, 0x000B001F],
                [0x0009001F, 0x0000001F, 0x0007001F, 0x0017001F, 0x0010001F],
                [0x0013001F, 0x000A001F, 0x0011001F, 0x0008001F, 0x0001001F],
                [0x0018001F, 0x000F001F, 0x0016001F, 0x000D001F, 0x0006001F],
                [0x000E001F, 0x0005001F, 0x000C001F, 0x0003001F, 0x0015001F]
                ]]
        return grid[self.gender][self.inc][self.dec]

    def nature_debug(self) -> str:
        grid = [
            ["Hardy", "Lonely", "Adamant", "Naughty", "Brave"],
            ["Bold", "Docile", "Impish", "Lax", "Relaxed"],
            ["Modest", "Mild", "Bashful", "Rash", "Quiet"],
            ["Calm", "Gentle", "Careful", "Quirky", "Sassy"],
            ["Timid", "Hasty", "Jolly", "Naive", "Serious"]
        ]
        return grid[self.inc][self.dec]

    def get_dec_stat(self) -> str:
        return self.stats[self.dec]

    def get_inc_stat(self) -> str:
        return self.stats[self.inc]

class PCRamData(NamedTuple):
    """
    Pokemon Colosseum Location RAM Representation. Any parameters can be left empty.

    Parameters
    --------
    ram_addr: The address of what needs to be checked or of the pointer

    ptr: If the ram_addr is a pointer or not

    ptr_offset: The offset of the ram_addr if it is a pointer

    bit_pos: The bit position if it is a bitflag address in the range of 0-7

    """
    ram_addr: Optional[int] = None
    ptr: bool = False
    ptr_offset: Optional[int] = None
    bit_pos: Optional[int] = None

class StringByteFunction:
    @staticmethod
    def string_to_bytes(user_string: str, encoded_length: int) -> bytes:
        """
        Encodes a provided string to UTF-8. Padding added until expected length is reached.
        Raise an exception if provided string is longer than provided length
        
        :param user_string: String to encode to bytes
        :param encoded_length: Expected length of provided string.
        """
        encoded_string = user_string.encode('utf-8')

        if len(encoded_string) < encoded_length:
            encoded_string += b'\x00' * (encoded_length - len(encoded_string))
        elif len(encoded_string) > encoded_length:
            raise Exception("Provided string '" + user_string + "' was langer than the expected byte length of '" + str(encoded_length) + "', which will not be accepted by the info file.")
        return encoded_string

    @staticmethod
    def byte_string_strip_null_terminator(bytes_input: bytes):
        return bytes_input.decode().strip("\0")
