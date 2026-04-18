import random

from worlds.pokemon_colo.iso_helper.fsys_helper.FsysFileEntry import REL, DataReadHelper

POKEMON_SLOT_OFFSET = 0x50
NEXT_MOVE_OFFSET = 0xA
START_OFFSET = 0x9FE28

class Offsets:
    class ByteStats:
        hp = 0x0
        atk = 0x1
        _def = 0x2
        spatk = 0x3
        spdef = 0x4
        spd = 0x5
    class Stats:
        hp = 0x0
        atk = 0x2
        _def = 0x4
        spatk = 0x6
        spdef = 0x8
        spd = 0x10
    class Move:
        pp = 0x4 # Usually just 0
        move = 0x6
    class Vars:
        ability = 0x0
        gender = 0x1
        nature = 0x2
        shadowId = 0x3
        level = 0x4
        aiRole = 0x6
        happiness = 0x8
        speciesId = 0xA
        pokeball = 0xC # What ball it comes out of (2 bytes)
        heldItemId = 0x10
        nameId = 0x14 # 4 bytes
        ivs = 0x1C # User ByteStats with this
        evs = 0x22 # Use Stats with this
        moveArrayStart = 0x30

class TrainerPokemon:
    """
    Internal representation of a Trainer's Pokemon. Functions may return false if fails (out of bounds for the trainer mostly)
    """
    
    pokemon_ids = []
    first_index = 0

    def __init__(self, first_index, rel_entry: REL):
        self.first_index = first_index
        self.rel_entry = rel_entry

    def test(self):
        slot_1 = (POKEMON_SLOT_OFFSET * self.first_index) + START_OFFSET
        DataReadHelper.write_int_to_bytes(self.rel_entry.data, slot_1 + Offsets.Vars.speciesId, random.choice(self.pokemon_ids), 2)
        slot_2 = slot_1 + POKEMON_SLOT_OFFSET
        DataReadHelper.write_int_to_bytes(self.rel_entry.data, slot_2 + Offsets.Vars.speciesId, random.choice(self.pokemon_ids), 2)
        