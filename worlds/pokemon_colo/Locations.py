from typing import NamedTuple, List
from BaseClasses import Location
from .Strings import Locations, Regions
from typing import Dict, List, TYPE_CHECKING
from .Options import ColosseumOptions, ColosseumSanity
from .Helpers import PCRamData, PCLocType
from .client.constants import *

if TYPE_CHECKING:
    from . import ColosseumWorld

class DebugInfo(NamedTuple):
    ptr_offset: int = -1
    bit: int = -1
    loc_name: str = ""

class PCLocData(NamedTuple):
    ram_info: PCRamData | List[PCRamData] = None
    map_id: List[int] = [-2] # To ensure that if a map ID is not important it is not unnecessarily checked in the client
    code: List[int] = [-1]
    type: PCLocType = PCLocType.NONE
    debug: DebugInfo = None

class ColosseumLocation(Location):
    game: str = "Pokemon Colosseum"


aidel_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED2, bit_pos=3)
emok_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E8, bit_pos=6)
calda_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC9, bit_pos=3)
kai_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F2, bit_pos=6)
pike_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F2, bit_pos=7)
geats_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=0)
geare_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=1)
loba_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=3)
akmen_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=2)
raleen_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=4)
tura_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=5)
toti_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=6)
elidi_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F1, bit_pos=7)
willie_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC5, bit_pos=7)
doken_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECE, bit_pos=2)
simes_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C103, bit_pos=5)
maiz_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=1)
rehan_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=4)
noxy_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=5)
twan_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=3)
valen_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=2)
sosh_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C103, bit_pos=1)
evat_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=6)
derid_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0FC, bit_pos=7)
zalo_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C103, bit_pos=0)
meli_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C103, bit_pos=2)
mela_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C103, bit_pos=3)
sema_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C103, bit_pos=4)

aidel1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0ED, bit_pos=5)
emok1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C178, bit_pos=5)
calda1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C178, bit_pos=2)
kai1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=2)
pike1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=3)
geats1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=4)
geare1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=5)
akmen1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=6)
loba1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=7)
raleen1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=0)
tura1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=1)
toti1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=2)
elidi1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=3)
willie1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECD, bit_pos=3)
doken1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF6, bit_pos=5)
simes1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=4)
maiz1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=5)
rehan1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=0)
noxy1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=1)
twan1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=7)
valen1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF0, bit_pos=6)
sosh1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=5)
evat1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=2)
derid1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=3)
zalo1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=4)
meli1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=6)
mela1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF7, bit_pos=7)
sema1_ram = PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF1, bit_pos=0)


start_locations: Dict[str, PCLocData] = {
    Locations.Misc.espeon_umbreon: PCLocData(ram_info=PCRamData(MAP_ID_ADDR), type=PCLocType.START, map_id=[OUTSKIRT_STAND_ID])
}

outside_city_locations: Dict[str, PCLocData] = {
    Locations.Trainers.willie: PCLocData(ram_info=[willie_ram, willie1_ram], type=PCLocType.TRAINER, map_id=[OUTSKIRT_STAND_ID]),
    Locations.Misc.bartender_gives_5_pokeballs: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECB, bit_pos=1), type=PCLocType.ITEM, map_id=[OUTSKIRT_STAND_ID])
}

phenac_locations: Dict[str, PCLocData] = {
    Locations.Misc.rui: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC4, bit_pos=5), type=PCLocType.EVENT, map_id=[PHENAC_CITY_ID]),
    Locations.Misc.tm41: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=0), type=PCLocType.ITEM, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.folly: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC4, bit_pos=4), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.wakin: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C11E, bit_pos=6), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.folly_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EA, bit_pos=6), type=PCLocType.TRAINER, map_id=[MAYOR_HOUSE_ID]),
    Locations.Trainers.trudly: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EA, bit_pos=7), type=PCLocType.TRAINER, map_id=[MAYOR_HOUSE_ID]),
    Locations.Trainers.kaib: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=0), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.drig: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECB, bit_pos=7), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.ShadowPokemon.makuhita_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=4), type=PCLocType.SHADOW, map_id=[MAYOR_HOUSE_ID]),
    Locations.Chests.phenac_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5F, bit_pos=4), type=PCLocType.CHEST, map_id=[PHENAC_CITY_ID])
}

# Array{Bayleef, Quilava, Croconaw}
starter_trainer_locations: Dict[str, PCLocData] = {
    Locations.Trainers.verde: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EF, bit_pos=7), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.rosso: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EE, bit_pos=0), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.bluno: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EE, bit_pos=1), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID])
}

starter_pokemon_captured: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.bayleef_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=5), type=PCLocType.SHADOW, map_id=[PHENAC_CITY_ID]),
    Locations.ShadowPokemon.quilava_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=6), type=PCLocType.SHADOW, map_id=[PHENAC_CITY_ID]),
    Locations.ShadowPokemon.croconaw_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=7), type=PCLocType.SHADOW, map_id=[PHENAC_CITY_ID])
}

starter_pokemon_purified: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.bayleef_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE9, bit_pos=5), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.quilava_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE9, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.croconaw_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE9, bit_pos=7), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID])
}

starter_trainer_locations_1: Dict[str, PCLocData] = {
    Locations.Trainers.verde_1: None,
    Locations.Trainers.rosso_1: None,
    Locations.Trainers.bluno_1: None
}

pregym_locations: Dict[str, PCLocData] = {
    Locations.Misc.complete_pre_gym: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=7), type=PCLocType.EVENT, map_id=[PREGYM_ID]),
    Locations.Trainers.botan: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=4), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.liqui: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=5), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.dugo: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=6), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.gwin: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=7), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.justy: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECD, bit_pos=6), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Misc.tm27: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECD, bit_pos=6), type=PCLocType.ITEM, map_id=[PREGYM_ID])
}

phenac_colosseum_r1_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm18: None,
    Locations.ColosseumTrainers.phenac_r1_1: None,
    Locations.ColosseumTrainers.phenac_r1_2: None,
    Locations.ColosseumTrainers.phenac_r1_3: None,
    Locations.ColosseumTrainers.phenac_r1_4: None,
    Locations.ColosseumTrainers.phenac_r1_win: None
}

phenac_colosseum_r2_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm11: None,
    Locations.ColosseumTrainers.phenac_r2_1: None,
    Locations.ColosseumTrainers.phenac_r2_2: None,
    Locations.ColosseumTrainers.phenac_r2_3: None,
    Locations.ColosseumTrainers.phenac_r2_4: None,
    Locations.ColosseumTrainers.phenac_r2_win: None
}

phenac_colosseum_r3_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm19: None,
    Locations.ColosseumTrainers.phenac_r3_1: None,
    Locations.ColosseumTrainers.phenac_r3_2: None,
    Locations.ColosseumTrainers.phenac_r3_3: None,
    Locations.ColosseumTrainers.phenac_r3_4: None,
    Locations.ColosseumTrainers.phenac_r3_win: None
}

phenac_colosseum_r4_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm22: None,
    Locations.ColosseumTrainers.phenac_r4_1: None,
    Locations.ColosseumTrainers.phenac_r4_2: None,
    Locations.ColosseumTrainers.phenac_r4_3: None,
    Locations.ColosseumTrainers.phenac_r4_4: None,
    Locations.ColosseumTrainers.phenac_r4_win: None
}

phenac_colosseum_locations = phenac_colosseum_r1_locations | phenac_colosseum_r2_locations | phenac_colosseum_r3_locations | phenac_colosseum_r4_locations

pyrite_locations: Dict[str, PCLocData] = {
    Locations.Trainers.hader: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C114, bit_pos=0), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.emok: PCLocData(ram_info=[emok_ram, emok1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.calda: PCLocData(ram_info=[calda_ram, calda1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    #TODO Lon, Vant, nover, diogo, leba, divel are all reset after you leave the screen. Connection loss or async run are a problem
    Locations.Trainers.lon: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDC3, bit_pos=5), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.vant: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDC3, bit_pos=4), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.nover: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDC3, bit_pos=0), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.diogo: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDC3, bit_pos=1), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.leba: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDC3, bit_pos=2), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.divel: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDC3, bit_pos=3), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.Trainers.cail: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EB, bit_pos=4), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.slugma_capture:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=7), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.misdreavus_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=4), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.noctowl_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=0), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.flaffy_capture:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=1), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.skiploom_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=2), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.quagsire_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=3), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.furret_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=6), type=PCLocType.SHADOW, map_id=[PYRITE_ID]),
    Locations.Misc.jail_key: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5F, bit_pos=5), type=PCLocType.ITEM, map_id=[PYRITE_POLICE_DEPARTMENT_ID]),
}

rematches_dakim_locations: Dict[str, PCLocData] = {
    Locations.Trainers.aidel_rematch: PCLocData(ram_info=aidel1_ram, type=PCLocType.REMATCH, map_id=[MT_BATTLE_OUTSIDE_ID]),
}

rematches_dakim_pyrite_locations: Dict[str, PCLocData] = {    
    Locations.Trainers.emok_rematch: PCLocData(ram_info=emok1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_ID]),
    Locations.Trainers.calda_rematch: PCLocData(ram_info=calda1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_ID]),
}

# TODO Rematches are reset when leaving the locations. The player has to be connected to the client otherwise progress may be lost
rematches_dakim_pyrite_building_and_cave_locations: Dict[str, PCLocData] = {
    Locations.Trainers.kai_rematch: PCLocData(ram_info=kai1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.Trainers.pike_rematch: PCLocData(ram_info=pike1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.Trainers.geats_rematch: PCLocData(ram_info=geats1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.geare_rematch: PCLocData(ram_info=geare1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.akmen_rematch: PCLocData(ram_info=akmen1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.loba_rematch: PCLocData(ram_info=loba1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.raleen_rematch: PCLocData(ram_info=raleen1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.tura_rematch: PCLocData(ram_info=tura1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.toti_rematch: PCLocData(ram_info=toti1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.elidi_rematch: PCLocData(ram_info=elidi1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.simes_rematch: PCLocData(ram_info=simes1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_ENTRANCE_ID]),
    Locations.Trainers.maiz_rematch: PCLocData(ram_info=maiz1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.Trainers.rehan_rematch: PCLocData(ram_info=rehan1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_1F_ID]),
    Locations.Trainers.noxy_rematch: PCLocData(ram_info=noxy1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_1F_ID]),
    Locations.Trainers.twan_rematch: PCLocData(ram_info=twan1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.Trainers.valen_rematch: PCLocData(ram_info=valen1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.Trainers.sosh_rematch: PCLocData(ram_info=sosh1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Trainers.evat_rematch: PCLocData(ram_info=evat1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_AFTER_SEWERS_ID]),
    Locations.Trainers.derid_rematch: PCLocData(ram_info=derid1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_AFTER_SEWERS_ID]),
    Locations.Trainers.meli_rematch: PCLocData(ram_info=meli1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Trainers.mela_rematch: PCLocData(ram_info=mela1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Trainers.sema_rematch: PCLocData(ram_info=sema1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_CAVE_SEWERS_ID]),
}

rematches_mirorb_locations: Dict[str, PCLocData] = {
    Locations.Trainers.willie_rematch: PCLocData(ram_info=willie1_ram, type=PCLocType.REMATCH, map_id=[OUTSKIRT_STAND_ID]),
    Locations.Trainers.doken_rematch: PCLocData(ram_info=doken1_ram, type=PCLocType.REMATCH, map_id=[PYRITE_BUILDING_ROOF_ID]),
}

pyrite_2_locations: Dict[str, PCLocData] = {
    Locations.Misc.elevator_key: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C117, bit_pos=1), type=PCLocType.ITEM, map_id=[PYRITE_POLICE_DEPARTMENT_ID]),
}

pyrite_jail_cell_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm46: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E4, bit_pos=7), type=PCLocType.ITEM, map_id=[PYRITE_POLICE_DEPARTMENT_ID])
}

construction_locations: Dict[str, PCLocData] = {
    Locations.Misc.windmill_gear: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC8, bit_pos=7), type=PCLocType.ITEM, map_id=[CONSTRUCTION_LOT_ID])
}

pyrite_colosseum_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm06: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C118, bit_pos=0), type=PCLocType.ITEM, map_id=[PYRITE_COLOSSEUM_ID]),
    Locations.ColosseumTrainers.pyrite_r0_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C12E, bit_pos=7), type=PCLocType.TRAINER, map_id=[PYRITE_COLOSSEUM_ID]),
    Locations.ColosseumTrainers.pyrite_r0_2: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C12D, bit_pos=0), type=PCLocType.TRAINER, map_id=[PYRITE_COLOSSEUM_ID]),
    Locations.ColosseumTrainers.pyrite_r0_3: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C12D, bit_pos=1), type=PCLocType.TRAINER, map_id=[PYRITE_COLOSSEUM_ID]),
    Locations.ColosseumTrainers.pyrite_r0_4: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECF, bit_pos=1), type=PCLocType.TRAINER, map_id=[PYRITE_COLOSSEUM_ID]),
    Locations.ColosseumTrainers.pyrite_r0_win: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECF, bit_pos=1), type=PCLocType.TRAINER, map_id=[PYRITE_COLOSSEUM_ID]),    
}

pyrite_building_1f_locations: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_h: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=6), type=PCLocType.ITEM, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.Trainers.nore: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDDC, bit_pos=4), type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.Trainers.kai: PCLocData(ram_info=[kai_ram, kai1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.Trainers.pike: PCLocData(ram_info=[pike_ram, pike1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.ShadowPokemon.yanma_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=5), type=PCLocType.SHADOW, map_id=[PYRITE_BUILDING_1F_ID]),
    Locations.Chests.pyrite_building_chest_3:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=0), type=PCLocType.CHEST, map_id=[PYRITE_BUILDING_1F_ID])
}

pyrite_building_2f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.geats: PCLocData(ram_info=[geats_ram, geats1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.geare: PCLocData(ram_info=[geare_ram, geare1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.loba: PCLocData(ram_info=[loba_ram, loba1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Trainers.akmen: PCLocData(ram_info=[akmen_ram, akmen1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_2F_ID]),
    Locations.Chests.pyrite_building_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=1), type=PCLocType.CHEST, map_id=[PYRITE_BUILDING_2F_ID])
}

pyrite_building_3f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.raleen: PCLocData(ram_info=[raleen_ram, raleen1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.tura: PCLocData(ram_info=[tura_ram, tura1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.toti: PCLocData(ram_info=[toti_ram, toti1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Trainers.elidi: PCLocData(ram_info=[elidi_ram, elidi1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_3F_ID]),
    Locations.Chests.pyrite_building_chest_2: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=2), type=PCLocType.CHEST, map_id=[PYRITE_BUILDING_3F_ID])
}

pyrite_building_roof_locations: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_s: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=3), type=PCLocType.ITEM, map_id=[PYRITE_BUILDING_ROOF_INSIDE_ID]),
    Locations.Trainers.reath: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECF, bit_pos=5), type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_ROOF_INSIDE_ID]),
    Locations.Trainers.ferma: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECF, bit_pos=6), type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_ROOF_INSIDE_ID]),
    Locations.Trainers.doken: PCLocData(ram_info=[doken_ram, doken1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_BUILDING_ROOF_ID]),
    Locations.ShadowPokemon.remoraid_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=0), type=PCLocType.SHADOW, map_id=[PYRITE_BUILDING_ROOF_INSIDE_ID]),
    Locations.ShadowPokemon.mantine_capture:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=1), type=PCLocType.SHADOW, map_id=[PYRITE_BUILDING_ROOF_INSIDE_ID]),
    Locations.ShadowPokemon.qwilfish_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=2), type=PCLocType.SHADOW, map_id=[PYRITE_BUILDING_ROOF_ID])
}

pyrite_building_locations = pyrite_building_1f_locations | pyrite_building_2f_locations | pyrite_building_3f_locations | pyrite_building_roof_locations

pyrite_cave_entrance_locations: Dict[str, PCLocData] = {
    Locations.Trainers.simes: PCLocData(ram_info=[simes_ram, simes1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_ENTRANCE_ID]),
    Locations.Chests.pyrite_cave_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=4), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_ENTRANCE_ID]),
    Locations.Chests.pyrite_cave_chest_2: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=5), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_ENTRANCE_ID])
}

pyrite_cave_1f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.rehan: PCLocData(ram_info=[rehan_ram, rehan1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_1F_ID]),
    Locations.Trainers.noxy: PCLocData(ram_info=[noxy_ram, noxy1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_1F_ID]),
    Locations.Chests.pyrite_cave_chest_3:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=6), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_1F_ID])
}

pyrite_cave_b1f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.maiz: PCLocData(ram_info=[maiz_ram, maiz1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.Trainers.twan: PCLocData(ram_info=[twan_ram, twan1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.Trainers.valen: PCLocData(ram_info=[valen_ram, valen1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.ShadowPokemon.meditite_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=3), type=PCLocType.SHADOW, map_id=[PYRITE_CAVE_B1F_ID]),
    Locations.Chests.pyrite_cave_chest_4: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5E, bit_pos=7), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_B1F_ID])
}

pyrite_cave_sewers_locations: Dict[str, PCLocData] = {
    Locations.Trainers.sosh: PCLocData(ram_info=[sosh_ram, sosh1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.ShadowPokemon.dunsparce_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=4), type=PCLocType.SHADOW, map_id=[PYRITE_CAVE_SEWERS_ID])
}

pyrite_cave_after_sewers_locations: Dict[str, PCLocData] = {
    Locations.Trainers.evat: PCLocData(ram_info=[evat_ram, evat1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_AFTER_SEWERS_ID]),
    Locations.Trainers.zalo: PCLocData(ram_info=[zalo_ram, zalo1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_AFTER_SEWERS_ID]),
    Locations.Trainers.derid: PCLocData(ram_info=[derid_ram, derid1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_AFTER_SEWERS_ID]),
    Locations.ShadowPokemon.swablu_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=5), type=PCLocType.SHADOW, map_id=[PYRITE_CAVE_AFTER_SEWERS_ID])
}

pyrite_cave_north_sewers_locations: Dict[str, PCLocData] = {
    Locations.Trainers.meli: PCLocData(ram_info=[meli_ram, meli1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Trainers.mela: PCLocData(ram_info=[mela_ram, mela1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Trainers.sema: PCLocData(ram_info=[sema_ram, sema1_ram], type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Chests.pyrite_cave_chest_5: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=1), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Chests.pyrite_cave_chest_6: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=2), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Chests.pyrite_cave_chest_7: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=3), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_SEWERS_ID]),
    Locations.Chests.pyrite_cave_chest_8: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=4), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_SEWERS_ID])
}

pyrite_cave_miror_hideout: Dict[str, PCLocData] = {
    Locations.Misc.plusle: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECE, bit_pos=5), type=PCLocType.EVENT, map_id=[PYRITE_CAVE_HIDEOUT_ID]),
    Locations.Misc.ein_file_p: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE62, bit_pos=7), type=PCLocType.ITEM, map_id=[PYRITE_CAVE_HIDEOUT_ID]),
    Locations.Trainers.mirorb: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECE, bit_pos=3), type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_HIDEOUT_ID]),
    Locations.Misc.mirorb_defeated: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECE, bit_pos=3), type=PCLocType.EVENT, map_id=[PYRITE_CAVE_HIDEOUT_ID]),
    Locations.ShadowPokemon.sudowoodo_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=6), type=PCLocType.SHADOW, map_id=[PYRITE_CAVE_HIDEOUT_ID]),
    Locations.Chests.pyrite_cave_chest_9: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C084, bit_pos=1), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_HIDEOUT_ID]),
    Locations.Chests.pyrite_cave_chest_10: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=5), type=PCLocType.CHEST, map_id=[PYRITE_CAVE_HIDEOUT_ID])
}

pyrite_cave_extra: Dict[str, PCLocData] = {
    #Can only be fought before defeating Evice, potentially missable if goal is different?
    Locations.Trainers.mirakleb: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF6, bit_pos=6), type=PCLocType.TRAINER, map_id=[PYRITE_CAVE_HIDEOUT_ID])
}

pyrite_cave_locations = pyrite_cave_entrance_locations | pyrite_cave_1f_locations | pyrite_cave_b1f_locations | pyrite_cave_sewers_locations | pyrite_cave_after_sewers_locations | pyrite_cave_north_sewers_locations | pyrite_cave_miror_hideout

agate_locations: Dict[str, PCLocData] = {
    Locations.Misc.small_tablet: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED3, bit_pos=2), type=PCLocType.ITEM, map_id=[AGATE_EUGEN_HOME_ID]),
    Locations.Misc.dukings_mail_read: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C122, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_EUGEN_HOME_ID]),
    Locations.Misc.master_ball: None,
    Locations.Trainers.skof: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C17E, bit_pos=3), type=PCLocType.TRAINER, map_id=[AGATE_ID]),
    Locations.Trainers.dury: None,
    Locations.Chests.agate_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5D, bit_pos=7), type=PCLocType.CHEST, map_id=[AGATE_ID]),
    Locations.Chests.agate_chest_2:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5C, bit_pos=0), type=PCLocType.CHEST, map_id=[AGATE_ID]),
    Locations.Chests.agate_chest_3: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE62, bit_pos=5), type=PCLocType.CHEST, map_id=[AGATE_SIDE_CAVE_ID]),
    Locations.Chests.agate_chest_4: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE62, bit_pos=6), type=PCLocType.CHEST, map_id=[AGATE_SIDE_CAVE_ID])
}

agate_locations_2: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_c: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5C, bit_pos=7), type=PCLocType.ITEM, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.Trainers.doven: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F6, bit_pos=0), type=PCLocType.TRAINER, map_id=[AGATE_MAIN_CAVE_ID]),
    Locations.Trainers.silton: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECC, bit_pos=1), type=PCLocType.TRAINER, map_id=[AGATE_MAIN_CAVE_ID]),
    Locations.Trainers.kass: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECC, bit_pos=4), type=PCLocType.TRAINER, map_id=[AGATE_MAIN_CAVE_ID]),
    Locations.Trainers.skrub: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED3, bit_pos=0), type=PCLocType.TRAINER, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.hitmontop_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07B, bit_pos=7), type=PCLocType.SHADOW, map_id=[AGATE_PURIFICATION_STONE_ID])
}

agate_locations = agate_locations | agate_locations_2

relic_stone_locations: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.makuhita_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE9, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.slugma_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=7), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.noctowl_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=0), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.flaffy_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=1), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.skiploom_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=2), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.quagsire_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.misdreavus_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.furret_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.yanma_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEE8, bit_pos=5), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.remoraid_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEF, bit_pos=0), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.mantine_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=1), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.qwilfish_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=2), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.meditite_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.dunsparce_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.swablu_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=5), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.sudowoodo_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.hitmontop_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=7), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.entei_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=0), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.ledian_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=1), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.suicune_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=2), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.gligar_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.stantler_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.piloswine_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=5), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.sneasel_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.aipom_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEE, bit_pos=7), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.murkrow_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=0), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.forretress_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=1), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.ariados_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.granbull_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=2), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.vibrava_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.raikou_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=5), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.sunflora_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.delibird_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEED, bit_pos=7), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.heracross_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=0), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.skarmory_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=1), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.miltank_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=2), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.absol_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.houndoom_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.tropius_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=5), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.metagross_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.tyranitar_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEEC, bit_pos=7), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID])
}

mt_battle_locations: Dict[str, PCLocData] = {
    Locations.Misc.f_disk: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE61, bit_pos=2), type=PCLocType.ITEM, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.turo: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0F6, bit_pos=5), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.drovic: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0ED, bit_pos=2), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.kimit: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E9, bit_pos=3), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.riden: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E9, bit_pos=2), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.telia: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E9, bit_pos=6), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.nortz: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E9, bit_pos=1), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.weeg: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E9, bit_pos=5), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.kison: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E8, bit_pos=5), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.berin: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E9, bit_pos=4), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.dakim: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C102, bit_pos=5), type=PCLocType.TRAINER, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Misc.dakim_defeated: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C102, bit_pos=5), type=PCLocType.EVENT, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Trainers.aidel: PCLocData(ram_info=[aidel_ram, aidel1_ram], type=PCLocType.TRAINER, map_id=[MT_BATTLE_OUTSIDE_ID]),
    Locations.ShadowPokemon.entei_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=0), type=PCLocType.SHADOW, map_id=[MT_BATTLE_PLATFORMS_1_ID]),
    Locations.Chests.mt_battle_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E4, bit_pos=4), type=PCLocType.CHEST, map_id=[MT_BATTLE_LOBBY_ID]),
    Locations.Misc.time_flute: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED2, bit_pos=2), type=PCLocType.ITEM, map_id=[MT_BATTLE_LOBBY_ID])
}

under_1_locations: Dict[str, PCLocData] = {
    Locations.Misc.powerup_part: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C119, bit_pos=6), type=PCLocType.ITEM, map_id=[THE_UNDER_ID]),
    Locations.Trainers.zada: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BDF2, bit_pos=3), type=PCLocType.TRAINER, map_id=[THE_UNDER_ID]),
    Locations.Trainers.gurks: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C114, bit_pos=2), type=PCLocType.TRAINER, map_id=[THE_UNDER_ID]),
    Locations.Chests.under_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE63, bit_pos=5), type=PCLocType.CHEST, map_id=[THE_UNDER_ID])
}

# TODO you dont need Power Up Part here (should we make it a requirement or not? Then Power Up Part is a useless item)
under_2_locations: Dict[str, PCLocData] = {
    Locations.Misc.r_disk: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED0, bit_pos=5), type=PCLocType.ITEM, map_id=[THE_UNDER_ID]),
    Locations.Trainers.kloak: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C13C, bit_pos=7), type=PCLocType.TRAINER, map_id=[THE_UNDER_ID]),
    Locations.Trainers.dagur: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED0, bit_pos=4), type=PCLocType.TRAINER, map_id=[THE_UNDER_ID]),
    Locations.ShadowPokemon.ledian_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=1), type=PCLocType.SHADOW, map_id=[THE_UNDER_ID])
}

under_forward_locations: Dict[str, PCLocData] = {

}

under_right_locations: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_f: None,
    Locations.Misc.subway_key: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE61, bit_pos=0), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.Trainers.venus: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED7, bit_pos=1), type=PCLocType.TRAINER, map_id=[THE_UNDER_RIGHT_ID]),
    Locations.Trainers.frena: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C107, bit_pos=6), type=PCLocType.TRAINER, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.Trainers.liaks: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C107, bit_pos=7), type=PCLocType.TRAINER, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.Trainers.lonia: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C106, bit_pos=0), type=PCLocType.TRAINER, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.Trainers.nelis: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BED7, bit_pos=5), type=PCLocType.TRAINER, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.ShadowPokemon.suicune_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=2), type=PCLocType.EVENT, map_id=[THE_UNDER_RIGHT_ID]),
    Locations.ShadowPokemon.gligar_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=3), type=PCLocType.EVENT, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.ShadowPokemon.stantler_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=4), type=PCLocType.EVENT, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.ShadowPokemon.piloswine_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=5), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.sneasel_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=6), type=PCLocType.EVENT, map_id=[]),
    Locations.Chests.under_chest_2: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE63, bit_pos=6), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_ID]),
    Locations.Chests.under_chest_3: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0E4, bit_pos=5), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_ID]),
    Locations.Chests.under_chest_4: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE62, bit_pos=1), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_B1F_SIDE_ID]),
    Locations.Chests.under_chest_5: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE62, bit_pos=0), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_B1F_SIDE_ID]),
    Locations.Chests.under_chest_6: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE63, bit_pos=7), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_B1F_ID]),
    Locations.Chests.under_chest_7:  PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE62, bit_pos=2), type=PCLocType.CHEST, map_id=[THE_UNDER_RIGHT_SUBWAY_ID])
}

under_up_locations: Dict[str, PCLocData] = {
    Locations.Chests.under_chest_8: None
}

under_locations = under_1_locations | under_2_locations | under_right_locations | under_up_locations

lab_subway_locations: Dict[str, PCLocData] = {
    Locations.Misc.maingate_key: None,
    Locations.Chests.lab_chest_2: None
}

lab_main_locations: Dict[str, PCLocData] = {
    Locations.Misc.dna_sample_1: None,
    Locations.Misc.down_st_key: None,
    Locations.Trainers.lethco: None,
    Locations.Trainers.cole: None,
    Locations.Trainers.odlow: None,
    Locations.Trainers.coren: None,
    Locations.ShadowPokemon.aipom_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C07A, bit_pos=7), type=PCLocType.EVENT, map_id=[])
}

lab_main_after_key_locations: Dict[str, PCLocData] = {
    Locations.Misc.dna_sample_2: None,
    Locations.Misc.dna_sample_3: None,
    Locations.Trainers.lare: None,
    Locations.Trainers.vana: None,
    Locations.Trainers.lesar: None,
    Locations.Trainers.tanie: None,
    Locations.Trainers.dubik: None,
    Locations.Trainers.kotan: None,
    Locations.Trainers.remil: None,
    Locations.ShadowPokemon.murkrow_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=0), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.forretress_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=1), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.ariados_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=4), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.granbull_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=2), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.vibrava_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=3), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.raikou_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=5), type=PCLocType.EVENT, map_id=[]),
    Locations.Chests.lab_chest_6: None,
}

lab_main_after_puzzle_locations: Dict[str, PCLocData] = {
    Locations.Misc.data_rom: None,
    Locations.Trainers.skrub_1: None,
    Locations.Trainers.ein: None,
    Locations.Chests.lab_chest_7: None
}

lab_shutter_locations: Dict[str, PCLocData] = {
    Locations.Misc.card_key: None,
    Locations.Trainers.myron: None,
    Locations.Chests.lab_chest_3: None,
    Locations.Chests.lab_chest_4: None,
    Locations.Chests.lab_chest_5: None
}

lab_outside_gate_locations: Dict[str, PCLocData] = {
    Locations.Misc.dukings_second_mail_received: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C170, bit_pos=1), type=PCLocType.EVENT, map_id=[LAB_OUTSIDE_ID]),
    Locations.Chests.lab_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5C, bit_pos=1), type=PCLocType.CHEST, map_id=[LAB_OUTSIDE_ID])
}

lab_locations = lab_outside_gate_locations | lab_subway_locations | lab_main_locations | lab_shutter_locations | lab_main_after_key_locations | lab_main_after_puzzle_locations

tower_pregate_locations: Dict[str, PCLocData] = {
    Locations.Misc.red_badge: None,
    Locations.Misc.grn_badge: None,
    Locations.Misc.blu_badge: None,
    Locations.Misc.ylw_badge: None,
    Locations.Trainers.bopen: None,
    Locations.Trainers.arton: None,
    Locations.Trainers.baila: None,
    Locations.Trainers.mirorb_1: None,
    Locations.Trainers.dakim_1: None,
    Locations.Trainers.venus_1: None,
    Locations.Trainers.ein_1: None,
    Locations.ShadowPokemon.delibird_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=7), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.sunflora_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C079, bit_pos=6), type=PCLocType.EVENT, map_id=[])
}

tower_postgate_locations: Dict[str, PCLocData] = {
    Locations.Trainers.dioge: None,
    Locations.Trainers.klest: None,
    Locations.Trainers.aline: None,
    Locations.Trainers.givern: None,
    Locations.Trainers.elose: None,
    Locations.Trainers.luper: None,
    Locations.Trainers.trus: None,
    Locations.Trainers.kevel: None,
    Locations.Trainers.rugen: None,
    Locations.Trainers.gonzap: None,
    Locations.ShadowPokemon.heracross_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=0), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.skarmory_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=1), type=PCLocType.EVENT, map_id=[])
}

tower_colosseum_locations: Dict[str, PCLocData] = {
    Locations.Trainers.jomas: None,
    Locations.Trainers.delan: None,
    Locations.Trainers.nella: None,
    Locations.Trainers.ston: None,
    Locations.Trainers.nascour: None,
    Locations.Trainers.evice: None,
    Locations.ShadowPokemon.miltank_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=2), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.absol_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=3), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.houndoom_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=4), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.tropius_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=5), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.metagross_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=6), type=PCLocType.EVENT, map_id=[]),
    Locations.ShadowPokemon.tyranitar_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C078, bit_pos=7), type=PCLocType.EVENT, map_id=[])
}

realgam_tower_locations = tower_pregate_locations | tower_postgate_locations | tower_colosseum_locations

postgame_purify: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.smeargle_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEF2, bit_pos=2), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.ursaring_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEF2, bit_pos=3), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.shuckle_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEF2, bit_pos=4), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
    Locations.ShadowPokemon.togetic_purify: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEF1, bit_pos=6), type=PCLocType.EVENT, map_id=[AGATE_PURIFICATION_STONE_ID]),
}

# Create helper variables to not have all_locations be so long
starter_pokemon = starter_trainer_locations | starter_pokemon_captured | starter_pokemon_purified | starter_trainer_locations_1
all_phenac = phenac_locations | pregym_locations | phenac_colosseum_locations
all_pyrite = pyrite_locations | pyrite_colosseum_locations | pyrite_building_locations | pyrite_cave_locations
all_agate = agate_locations | relic_stone_locations
all_postgame = postgame_purify

all_locations = start_locations | starter_pokemon | outside_city_locations | all_phenac | all_pyrite | all_agate | all_postgame | construction_locations | mt_battle_locations | pyrite_cave_extra | pyrite_2_locations | pyrite_jail_cell_locations | under_locations | lab_locations | realgam_tower_locations

regions_to_locations: Dict[str, Dict[str, PCLocData]] = {
    Regions.menu: start_locations,
    Regions.rematch: [], # Do not put any locations here, this is to seperate rematch regions into their own seperate master region node
    Regions.phenac: [], # Dynamically modified
    Regions.phenac_city_pregym: pregym_locations,
    Regions.phenac_colosseum: [],
    Regions.phenac_colosseum_r2: [],
    Regions.phenac_colosseum_r3: [],
    Regions.phenac_colosseum_r4: [],
    Regions.outside_city: outside_city_locations,
    Regions.rematches_dakim: rematches_dakim_locations,
    Regions.rematches_dakim_pyrite: rematches_dakim_pyrite_locations,
    Regions.rematches_dakim_pyrite_building_and_cave: rematches_dakim_pyrite_building_and_cave_locations,
    Regions.rematches_mirorb: rematches_mirorb_locations,
    Regions.pyrite: pyrite_locations,
    Regions.pyrite_building : pyrite_building_locations,
    Regions.pyrite_cave: [], # Dynamically modified
    Regions.the_under: under_1_locations,
    Regions.the_under_2: under_2_locations,
    Regions.the_under_f: [],
    Regions.the_under_r: under_right_locations,
    Regions.the_under_u: under_up_locations,
    Regions.under_colosseum: [],
    Regions.under_colosseum_r2: [],
    Regions.under_colosseum_r3: [],
    Regions.under_colosseum_r4: [],
    Regions.pyrite_colosseum: pyrite_colosseum_locations,
    Regions.pyrite_colosseum_r1: [],
    Regions.pyrite_colosseum_r2: [],
    Regions.pyrite_colosseum_r3: [],
    Regions.pyrite_colosseum_r4: [],
    Regions.pyrite_2: pyrite_2_locations,
    Regions.pyrite_jail_cell: pyrite_jail_cell_locations,
    Regions.construction: construction_locations,
    Regions.agate: agate_locations,
    Regions.purify: [],
    Regions.mt_battle: mt_battle_locations,
    Regions.lab: lab_outside_gate_locations,
    Regions.lab_shutter: lab_shutter_locations,
    Regions.lab_main: lab_main_locations,
    Regions.lab_main_after_key: lab_main_after_key_locations,
    Regions.lab_main_after_puzzle: lab_main_after_puzzle_locations,
    Regions.lab_station: lab_subway_locations,
    Regions.realgam: tower_pregate_locations,
    Regions.pre_final: [], # Dynamically modified
    Regions.final: tower_colosseum_locations,
    Regions.snagem: [],
}

# Local lists for dynamic allocation of Dicts
starter_trainer_locations_list = [
    Locations.Trainers.verde,
    Locations.Trainers.rosso,
    Locations.Trainers.bluno
]

starter_pokemon_captured_list = [
    Locations.ShadowPokemon.bayleef_capture,
    Locations.ShadowPokemon.quilava_capture,
    Locations.ShadowPokemon.croconaw_capture
]

starter_trainer_locations_1_list = [
    Locations.Trainers.verde_1,
    Locations.Trainers.rosso_1,
    Locations.Trainers.bluno_1
]

def set_location_options(options: ColosseumOptions) -> Dict[str, Dict[str, PCLocData]]:
    local_regions = regions_to_locations.copy()
    local_phenac = phenac_locations.copy()
    local_relic = relic_stone_locations.copy()
    local_tower = tower_postgate_locations.copy()
    local_cave = pyrite_cave_locations.copy()

    trainer = starter_trainer_locations_list[options.phenac_starter_choice]
    starter = starter_pokemon_captured_list[options.phenac_starter_choice]
    trainer_1 = starter_trainer_locations_1_list[options.phenac_starter_choice]

    # Dynamic allocations of locally created Dicts for all game locations
    local_phenac[trainer] = starter_trainer_locations[trainer]
    local_phenac[starter] = starter_pokemon_captured[starter]
    local_relic.update(starter_pokemon_purified)
    local_tower[trainer_1] = starter_trainer_locations_1[trainer_1]

    if options.postgame_shadow_pokemon:
        local_relic.update(postgame_purify)

    if options.mirakle_b: 
        local_cave.update(pyrite_cave_extra)

    if options.colosseum_sanity != ColosseumSanity.option_off:
        local_regions[Regions.phenac_colosseum] = phenac_colosseum_r1_locations
        local_regions[Regions.phenac_colosseum_r2] = phenac_colosseum_r2_locations
        local_regions[Regions.phenac_colosseum_r3] = phenac_colosseum_r3_locations
        local_regions[Regions.phenac_colosseum_r4] = phenac_colosseum_r4_locations

    local_regions[Regions.phenac] = local_phenac
    local_regions[Regions.pyrite_cave] = local_cave
    local_regions[Regions.purify] = local_relic
    local_regions[Regions.pre_final] = local_tower

    if not options.rematches:
        local_regions[Regions.rematches_dakim] = {}
        local_regions[Regions.rematches_dakim_pyrite] = {}
        local_regions[Regions.rematches_dakim_pyrite_building_and_cave] = {}
        local_regions[Regions.rematches_mirorb] = {}

    return local_regions
