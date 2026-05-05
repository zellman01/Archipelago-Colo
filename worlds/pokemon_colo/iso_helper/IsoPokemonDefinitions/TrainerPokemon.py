import random

from worlds.pokemon_colo.iso_helper.IsoPokemonDefinitions.Pokemon import Pokemon
from worlds.pokemon_colo.iso_helper.fsys_helper.FsysFileEntry import REL, DataReadHelper
from worlds.pokemon_colo.Options import Difficulty, Randomizer
from worlds.pokemon_colo.Helpers import StatGen

POKEMON_SLOT_OFFSET = 0x50
NEXT_MOVE_OFFSET = 0xA
START_OFFSET = 0x9FE28
EASY_DIFFICULTY_MODIFIER = 5
HARD_DIFFICULTY_MODIFIER = 10
EXTREME_DIFFICULTY_MODIFIER = 15

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
        level = 0x4 # 1 byte
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

    def generation(self, slotAmount, dif: Difficulty, random: Randomizer) -> bool:
        """
        Runs the generation/modifying code for trainers based on AP world settings.
        Returns false only if the slotAmount is out of range

        :param slotAmount: The total amount of slots for the given trainer (max: 6 min: 2)
        :param dif: The Difficulty Options class
        :param random: The Randomizer Options class
        """
        if slotAmount > 6 or slotAmount < 2:
            return False
        levelMod = 0
        if dif == Difficulty.option_easy:
            levelMod = -EASY_DIFFICULTY_MODIFIER # Downward adjustment
        elif dif == Difficulty.option_hard:
            levelMod = HARD_DIFFICULTY_MODIFIER
        elif dif == Difficulty.option_extreme:
            levelMod = EXTREME_DIFFICULTY_MODIFIER
        for i in range(0, slotAmount):
            self.modify_slot_start(i, levelMod, random)
        return True

    def modify_slot_start(self, slot_num, level_mod, random_yes: Randomizer):
        """
        Will modify opponent trainer's slots. Will do nothing if above the max amount it normally has.
        """
        slot_offset = START_OFFSET + (POKEMON_SLOT_OFFSET * self.first_index) + (POKEMON_SLOT_OFFSET * slot_num)
        used = DataReadHelper.int_from_bytes(self.rel_entry.data, slot_offset + Offsets.Vars.speciesId, 2) != 0
        if used:
            self.modify_slot(slot_offset, level_mod, random_yes)

    def modify_slot(self, slot_offset, level_mod, random_yes: Randomizer): # To modify a slot
        if random_yes:
            DataReadHelper.write_int_to_bytes(self.rel_entry.data, slot_offset + Offsets.Vars.speciesId, random.choice(self.pokemon_ids), 2)
        if level_mod != 0:
            tmpLevel = DataReadHelper.int_from_bytes(self.rel_entry.data, slot_offset + Offsets.Vars.level, 1)
            tmpLevel += level_mod
            DataReadHelper.write_int_to_bytes(self.rel_entry.data, slot_offset + Offsets.Vars.level, tmpLevel, 1)