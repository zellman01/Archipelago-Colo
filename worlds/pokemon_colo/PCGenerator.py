import json, os
from random import Random
import struct

import Utils

from CommonClient import logger

from gclib.gcm import GCM

from .iso_helper.fsys_helper.FsysFileDetail import FileType
from .iso_helper.IsoPokemonDefinitions.Pokemarts import Pokemart
from .iso_helper.fsys_helper.FsysFileEntry import REL
from .iso_helper.fsys_helper.FsysFile import FsysFile
from .Helpers import StringByteFunction as sbf
from .client.constants import CLIENT_VERSION, AP_WORLD_VERSION_NAME

class ColosseumRandomizer:
    def __init__(self, iso_path: str, randomized_output_file_path: str, ap_output_data: bytes, debug_flag=False):
        # Notes randomized folder path and if files should be exported instead of making an ISO
        self.debug = debug_flag
        self.clean_iso_path = iso_path
        self.randomized_output_file_path = randomized_output_file_path

        try:
            if os.path.isfile(randomized_output_file_path):
                tmp_file = open(randomized_output_file_path, "r+")
                tmp_file.close()
        except IOError:
            raise Exception("'" + randomized_output_file_path + "' is currently in use by another application.")

        self.output_data = json.loads(ap_output_data.decode('utf-8'))

        # Server and client version need to match before continuing
        self._check_versions(self.output_data)

        # Read entire ISO contents into memory
        self.gcm = GCM(self.clean_iso_path)
        self.gcm.read_entire_disc()

        # Set random seed
        self.random = Random()
        local_seed: str = str(self.output_data["Seed"])
        self.random.seed(local_seed)

        # Game ID change for save files to be different
        logger.info("Update ISO game ID locations with AP generated seed")
        three_char_seed = local_seed[:3]
        bin_data = self.gcm.read_file_data("sys/boot.bin")
        bin_data.seek(0x00)
        bin_data.write(sbf.string_to_bytes(three_char_seed, len(three_char_seed)))
        dol_data = self.gcm.read_file_data("sys/main.dol")
        dol_data.seek(0x399B74)
        dol_data.write(sbf.string_to_bytes(three_char_seed, len(three_char_seed)))
        dol_data.seek(0x39A754)
        dol_data.write(sbf.string_to_bytes(three_char_seed, len(three_char_seed)))

        # Inject custom code
        self.inject_custom_code(dol_data)

        self.gcm.changed_files["sys/boot.bin"] = bin_data
        self.gcm.changed_files["sys/main.dol"] = dol_data

        # Change the Outskirt Stand to have a pokeballs instead of a antidote in the shop form the beginning
        # Proof of Concept implementatoin, can be used for Shopsanity or balancing
        pocket_menu = self.gcm.read_file_data("files/pocket_menu.fsys")
        pocket_menu_fsys = FsysFile("pocket_menu.fsys", pocket_menu)
        pocket_menu_rel = pocket_menu_fsys.get_entry_by_filename("pocket_menu", FileType.REL)

        if (isinstance(pocket_menu_rel, REL)):
            outskirts_mart_before_pokeballs = Pokemart(0, pocket_menu_rel)
            outskirts_mart_before_pokeballs.write_item_at_index(0x0003, 0) 
            outskirts_mart_before_pokeballs.write_item_at_index(0x0004, 1) 

        pocket_menu_fsys.encode_and_write_to_stream()
        self.gcm.changed_files["files/pocket_menu.fsys"] = pocket_menu

        

        # Handle rest of game randomization/AP related modifications to files


        # Saves randomized iso file, with files updated
        self.save_randomized_iso()

    def inject_custom_code(self, dol_data):
        # We inject our code into this line. It is called a few times after changing rooms or events
        # Not quite sure what the method does, but it gets called often so we can inject custom code here
        addr_caller = self.t1_memroy_to_dol_address(0x801904e8)
        caller_method = [
            0x4BE72FF9,  # bl    0x800034E0
        ]
        dol_data.seek(addr_caller)
        for instr in caller_method:
            dol_data.write(struct.pack(">I", instr))

        # We inject our code into the T0 section where there are a lot of empty bytes scattered around
        # We can use them to place our function into main.dol
        # On load it gets loaded into the memory range of T0
        # We can place custom code here, for example to modfiy items to be always available and not missable
        # This is just a test for now. These bits could also be changed through the client, but would require it to be open
        # all the time in order to play the game. So more critical stuff can be placed here directly into the iso
        addr_code = self.t0_memroy_to_dol_address(0x800034E0)        
        custom_method = [
            0x7C1E212E,  # stwx  r0, r30, r4  (original replaced instruction)

            # Load primary pointer
            0x3CA08048,  # lis   r5, 0x8048
            0x80A5ADB8,  # lwz   r5, 0xADB8(r5)    r5 = *(0x8047ADB8)

            # Makes Tm46 always visible (still needs jail key)
            # Set bit 0 (*(ptr) + 0x1C177)
            0x3CE50002,  # addis r7, r5, 2         r7 = r5 + 0x20000
            0x88C7C177,  # lbz   r6, 0xC177(r7)
            0x60C60001,  # ori   r6, r6, 0x0001
            0x98C7C177,  # stb   r6, 0xC177(r7)

            # Makes Jail Key always visible (no story needed and cant miss it if other locations are visited first)
            # Set bit 5 (*(ptr) + 0x1C119)
            0x88C7C119,  # lbz   r6, 0xC119(r7)
            0x60C60020,  # ori   r6, r6, 0x0020
            0x98C7C119,  # stb   r6, 0xC119(r7)

            0x4E800020,  # blr
        ]
        dol_data.seek(addr_code)
        for instr in custom_method:
            dol_data.write(struct.pack(">I", instr))
            
    def t0_memroy_to_dol_address(self, mem_address):
        return 0x100 + (mem_address - 0x80003100)

    def t1_memroy_to_dol_address(self, mem_address):
        return 0x25E0 + (mem_address - 0x800055e0)

    def _check_versions(self, output_data):
        """
        Compares patch version with client's version
        
        :param output_data: The patch's output data where we attempt to aquire the generated version.
        """
        ap_world_version="<0.1.0"

        if AP_WORLD_VERSION_NAME in output_data:
            ap_world_version = output_data[AP_WORLD_VERSION_NAME]
        if ap_world_version != CLIENT_VERSION:
            raise Utils.VersionException("Error! Server was generated with a different Pokemon Colosseum " +
                        f"APWorld Version.\nThe client version is {CLIENT_VERSION}, which is incompatable with the given version of {ap_world_version}.")

    def save_randomized_iso(self):
        for _, _ in self.export_files_from_memory():
            continue

    def export_files_from_memory(self):
        yield from self.gcm.export_disc_to_iso_with_changed_files(self.randomized_output_file_path)

if __name__ == '__main__':
    print("Run this from Launcher.py instead")
