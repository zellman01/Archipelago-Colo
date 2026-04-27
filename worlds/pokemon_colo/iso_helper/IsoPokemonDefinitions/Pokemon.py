# To modify pokemon base stats and learnable TMs in the common.rel file

from worlds.pokemon_colo.iso_helper.fsys_helper.FsysFileEntry import REL, DataReadHelper

POKEMON_DATA_START = 0x123250
POKEMON_STRUCT_LEN = 0x11C

class Offsets:
    class Stats:
        # All 2 bytes
        hp = 0x0
        attack = 0x2
        defense = 0x4
        spatk = 0x6
        spdef = 0x8
        speed = 0xA
    class Evolution:
        method = 0x0
        condition = 0x2
        form = 0x4
    class LevelMove:
        level = 0x0
        move = 0x2
    class Sprites:
        pokedex_color = 0x0
        face_id = 0x2
        body_id = 0x4
    class Vars:
        ability_1_offset = 0x32
        ability_2_offset = 0x33
        tm01_offset = 0x34
        hm01_offset = 0x66
        base_offset = 0x84

class Pokemon:
    internal_id: int = 0 # NOT the same as national pokedex for any Gen 3 Pokemon

    def __init__(self, id, rel_entry: REL):
        self.internal_id = id
        self.rel_entry = rel_entry

        self.pokemon_offset_addr = POKEMON_DATA_START + (POKEMON_STRUCT_LEN * self.internal_id)

    def get_base_stat(self, offset) -> int:
        return DataReadHelper.int_from_bytes(self.rel_entry, self.pokemon_offset_addr + Offsets.Vars.base_offset + offset, 2)

    def get_hp(self) -> int:
        return self.get_base_stat(Offsets.Stats.hp)

    def get_attack(self) -> int:
        return self.get_base_stat(Offsets.Stats.attack)

    def get_defense(self) -> int:
        return self.get_base_stat(Offsets.Stats.defense)

    def get_sp_attack(self) -> int:
        return self.get_base_stat(Offsets.Stats.spatk)

    def get_sp_defense(self) -> int:
        return self.get_base_stat(Offsets.Stats.spdef)

    def get_speed(self) -> int:
        return self.get_base_stat(Offsets.Stats.speed)