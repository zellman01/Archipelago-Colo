import math, random
from typing import List

from .Helpers import Nature
from .Items import ItemDesc


class ShadowData:
    byte_total = 222

    def __init__(self, pc_item: ItemDesc, ot: str, ot_id: int, name: str):
        self.id = pc_item["data"].item_id
        self.ot = ot
        self.ot_id = ot_id
        self.ball = 4
        self.unknown = 0x0B030202
        self.nickname = name
        self.level = pc_item["data"].level # Both level and met level
        self.shadow_id = pc_item["data"].shadow_id
        gender = random.randrange(0,2)
        inc_stat = random.randrange(0,5)
        dec_stat = random.randrange(0,5)
        self.nature = Nature(dec_stat, inc_stat, gender)
        self.hp_iv = random.randrange(0,32)
        self.atk_iv = random.randrange(0,32)
        self.def_iv = random.randrange(0,32)
        self.sp_atk_iv = random.randrange(0,32)
        self.sp_def_iv = random.randrange(0,32)
        self.spd_iv = random.randrange(0,32)
        # TODO: Figure out how to get base stat for the given pokemon (maybe incorporate it in the item data?)
        self.hp = self.calc_hp(self.level, 0, self.hp_iv)
        self.atk = self.calc_other_stat(self.level, 0, self.atk_iv, self.modify_nature_value("Atk"))
        self._def = self.calc_other_stat(self.level, 0, self.def_iv, self.modify_nature_value("Def"))
        self.sp_atk = self.calc_other_stat(self.level, 0, self.sp_atk_iv, self.modify_nature_value("Sp. Atk"))
        self.sp_def = self.calc_other_stat(self.level, 0, self.sp_def_iv, self.modify_nature_value("Sp. Def"))
        self.spd = self.calc_other_stat(self.level, 0, self.spd_iv, self.modify_nature_value("Spd"))
        self.move_1_id = pc_item["data"].move_id[0]
        self.move_1_pp = pc_item["data"].move_pp[0]
        self.move_2_id = pc_item["data"].move_id[1]
        self.move_2_pp = pc_item["data"].move_pp[1]
        self.move_3_id = pc_item["data"].move_id[2]
        self.move_3_pp = pc_item["data"].move_pp[2]
        self.move_4_id = pc_item["data"].move_id[3]
        self.move_4_pp = pc_item["data"].move_pp[3]

    def debug(self) -> str:
        return f"Nature: {self.nature.nature_debug()}\n\
            OT: {self.ot}\n\
            Nickname: {self.nickname}\n"

    def modify_nature_value(self, stat: str) -> float:
        value = 1.0
        if self.nature.get_inc_stat() == self.nature.get_dec_stat():
            pass
        elif self.nature.get_inc_stat() == stat:
            value = 1.1
        elif self.nature.get_dec_stat() == stat:
            value = 0.9
        
        return value

    def get_move(self, move_num: int) -> List[bytes]:
        """
        Get move based on number

        Parameters
        ------
        move_num: Which move to get. Range of 1-4

        Returns
        ------
        List of id, pp in that order as bytes. Will be empty if outside of the range
        """
        ret_value: List[bytes] = []
        match move_num:
            case 1:
                ret_value.insert(0, int.to_bytes(self.move_1_id, 2))
                ret_value.insert(1, int.to_bytes(self.move_1_pp, 2))
            case 2:
                ret_value.insert(0, int.to_bytes(self.move_2_id, 2))
                ret_value.insert(1, int.to_bytes(self.move_2_pp, 2))
            case 3:
                ret_value.insert(0, int.to_bytes(self.move_3_id, 2))
                ret_value.insert(1, int.to_bytes(self.move_3_pp, 2))
            case 4:
                ret_value.insert(0, int.to_bytes(self.move_4_id, 2))
                ret_value.insert(1, int.to_bytes(self.move_4_pp, 2))
        return ret_value

    def combine_moves(self):
        return b''.join([int.to_bytes(self.move_1_id, 2), int.to_bytes(self.move_1_pp, 2), int.to_bytes(self.move_2_id, 2), int.to_bytes(self.move_2_pp, 2), 
                            int.to_bytes(self.move_3_id, 2), int.to_bytes(self.move_3_pp, 2), int.to_bytes(self.move_4_id, 2), int.to_bytes(self.move_4_pp, 2)])

    def verify_bytes(self):
        poke_bytes = self.__bytes__()
        if len(poke_bytes) == self.byte_total:
            return poke_bytes
        else:
            raise Exception(f"Was expecting Pokemon data to be {self.byte_total} length, got {len(poke_bytes)} instead.")

    def __bytes__(self) -> bytes: # Useless function, keeping it here as it documents internal pokemon data structure for now
        b_id = int.to_bytes(self.id, 2)
        b_unknown = int.to_bytes(0x0, 2)
        b_nature = int.to_bytes(self.nature.nature_hex(), 4)
        b_required = int.to_bytes(self.unknown, 4)
        b_met_loc = int.to_bytes(0x0, 2)
        b_level = int.to_bytes(self.level, 1) # Used twice, met location and starting level
        b_pokeball = int.to_bytes(self.ball, 1)
        b_unknown_2 = int.to_bytes(0x0, 6)
        b_ot_id = int.to_bytes(self.ot_id, 2)
        b_ot_name = self.string_bytes(list(self.ot), 20)
        b_nickname = self.string_bytes(list(self.nickname), 22)
        b_unknown_3 = int.to_bytes(0x0, 2)
        b_exp = int.to_bytes(0x0, 4) # TODO: Figure out what this value needs to be based on pokemon and level
        b_unknown_4 = int.to_bytes(0x0, 23)
        b_moves = self.combine_moves()
        b_held_item = int.to_bytes(0x0, 2) # TODO: Get default held item for pokemon
        b_stats = b''.join([int.to_bytes(self.hp, 2), int.to_bytes(self.hp, 2), int.to_bytes(self.atk, 2),
                               int.to_bytes(self._def, 2), int.to_bytes(self.sp_atk, 2), int.to_bytes(self.sp_def, 2), int.to_bytes(self.spd, 2)])
        b_ev = int.to_bytes(0x0, 12) # For all the EV stats
        b_iv = b''.join([int.to_bytes(self.hp_iv, 2), int.to_bytes(self.atk_iv, 2), int.to_bytes(self.def_iv, 2), int.to_bytes(self.sp_atk_iv, 2),
                            int.to_bytes(self.sp_def_iv, 2), int.to_bytes(self.spd_iv, 2)])
        b_unknown_5 = int.to_bytes(0x0, 1)
        b_friendship = int.to_bytes(0x0, 1)
        b_unknown_6 = int.to_bytes(0x0, 5)
        b_ribbons_1 = int.to_bytes(0x0, 15)
        b_shadow_clear_ribbon = int.to_bytes(0x0, 1) # TODO: Check if shadow pokemon has already been purified when being given, then award this ribbon if so
        b_ribbons_2 = int.to_bytes(0x0, 2)
        b_unknown_7 = int.to_bytes(0x0, 1)
        b_pokerus_on = int.to_bytes(0x0, 1)
        b_unknown_8 = int.to_bytes(0x0, 14)
        b_shadow_id = int.to_bytes(self.shadow_id, 1)
        # TODO: Figure out what these values actually do to the pokemon
        b_shadow_check_1 = int.to_bytes(0xCD, 1)
        b_shadow_check_2 = int.to_bytes(0xDC, 1)
        b_shadow_gauge = int.to_bytes(0xCDDC, 2)
        return b''.join([b_id, b_unknown, b_nature, b_required, b_met_loc, b_level, b_pokeball, b_unknown_2, b_ot_id, b_ot_name, b_nickname, b_nickname, b_unknown_3, b_exp, b_level,
                            b_unknown_4, b_moves, b_held_item, b_stats, b_ev, b_iv, b_unknown_5, b_friendship, b_unknown_6, b_ribbons_1, b_shadow_clear_ribbon, b_ribbons_2,
                            b_unknown_7, b_pokerus_on, b_unknown_8, b_shadow_id, b_shadow_check_1, b_shadow_check_2, b_shadow_gauge])

    def string_bytes(self, string: list, max: int) -> bytes:
        byte_list = list()
        for i in range(len(string)):
            byte_list.append(int.to_bytes(0x0, 1))
            byte_list.append(int.to_bytes(ord(string[i]), 1))
        step_two = len(string)-max
        for _ in range(step_two, max):
            byte_list.append(int.to_bytes(0x0, 1))
        return b''.join(byte_list)

    def calc_hp(self, level: int, base: int, iv: int) -> int:
        return math.floor(((2*base+iv)*level)/100)+level+10

    def calc_other_stat(self, level: int, base: int, iv: int, nature: float) -> int:
        return int(math.floor(((((2*base+iv)*level)/100)+5)*nature))

