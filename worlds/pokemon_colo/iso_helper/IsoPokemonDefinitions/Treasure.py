from worlds.pokemon_colo.iso_helper.fsys_helper.FsysFileEntry import REL, DataReadHelper

class Treasure:
    def __init__(self, treasure_id: int, rel_entry: REL):
        self.rel_entry = rel_entry
        self.id = treasure_id
        self.start = 0x11D7F8+(0x1C*treasure_id)

    def modify_quantity(self, quantity: int):
        return DataReadHelper.write_int_to_bytes(self.rel_entry.data, self.start+1, quantity, 1)

    def modify_item(self, item_id: int):
        return DataReadHelper.write_int_to_bytes(self.rel_entry.data, self.start+0xC, item_id, 4)