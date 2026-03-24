from worlds.pokemon_colo.iso_helper.fsys_helper.FsysFileEntry import REL, DataReadHelper

NUMBER_OF_POKEMARTS_POINTER_INDEX = 5
POKEMON_ITEMS_POINTER_INDEX= 2
POKEMON_ITEM_START_OFFSET_POINTER_INDEX = 4

class Pokemart:
    number_of_items = 0

    def __init__(self, id, rel_entry: REL):
        self.id = id
        self.rel_entry = rel_entry

        item_start_index = self.__get_first_item_offset()
        end = False
        while not end:
            item_id = DataReadHelper.int_from_bytes(self.rel_entry.data, self.rel_entry.get_pointer(POKEMON_ITEMS_POINTER_INDEX) + item_start_index, 2)
            item_start_index += 2
            if item_id == 0:
                end = True
            else:
                self.number_of_items += 1

            if self.number_of_items > 100:
                raise Exception("Too many items in mart with id " + str(id) + ". Found " + str(self.number_of_items) + " items.")
  
    def write_item_at_index(self, item_id, index):
        if index >= self.number_of_items:
            raise Exception("Item index " + str(index) + " is out of bounds for mart with id " + str(self.id) + " which has " + str(self.number_of_items) + " items.")
        item_offset = self.__get_first_item_offset() + (index * 2)
        return DataReadHelper.write_int_to_bytes(self.rel_entry.data, self.rel_entry.get_pointer(POKEMON_ITEMS_POINTER_INDEX) + item_offset, item_id, 2)

    def get_item_at_index(self, index):
        if index >= self.number_of_items:
            raise Exception("Item index " + str(index) + " is out of bounds for mart with id " + str(self.id) + " which has " + str(self.number_of_items) + " items.")
        item_offset = self.__get_first_item_offset() + (index * 2)
        return DataReadHelper.int_from_bytes(self.rel_entry.data, self.rel_entry.get_pointer(POKEMON_ITEMS_POINTER_INDEX) + item_offset, 2)

    def __get_first_item_offset(self):
        return DataReadHelper.int_from_bytes(self.rel_entry.data, self.rel_entry.get_pointer(POKEMON_ITEM_START_OFFSET_POINTER_INDEX) + (self.id * 4) + 2, 2) * 2
        

    