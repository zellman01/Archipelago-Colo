import enum
from .Strings import Locations, Items

class Pokemon(enum.Enum):
    MAKUHITA = (Items.Progression.makuhita, True, 0x1, Locations.ShadowPokemon.makuhita_capture)
    BAYLEAF = (Items.Progression.bayleef, True, 0x2, Locations.ShadowPokemon.bayleef_capture)
    QUILAVA = (Items.Progression.quilava, True, 0x3, Locations.ShadowPokemon.quilava_capture)
    CROCONAW = (Items.Progression.croconaw, True, 0x4, Locations.ShadowPokemon.croconaw_capture)
    SLUGMA = (Items.Progression.slugma, True, 0x5, Locations.ShadowPokemon.slugma_capture)
    NOCTOWL = (Items.Progression.noctowl, True, 0x6, Locations.ShadowPokemon.noctowl_capture)
    FLAFFY = (Items.Progression.flaffy, True, 0x7, Locations.ShadowPokemon.flaffy_capture)
    SKIPLOOM = (Items.Progression.skiploom, True, 0x8, Locations.ShadowPokemon.skiploom_capture)
    QUAGSIRE = (Items.Progression.quagsire, True, 0x9, Locations.ShadowPokemon.quagsire_capture)
    MISDREAVUS = (Items.Progression.misdreavus, True, 0xA, Locations.ShadowPokemon.misdreavus_capture)
    FURRET = (Items.Progression.furret, True, 0xB, Locations.ShadowPokemon.furret_capture)
    YANMA = (Items.Progression.yanma, True, 0xC, Locations.ShadowPokemon.yanma_capture)
    REMORAID = (Items.Progression.remoraid, True, 0xD, Locations.ShadowPokemon.remoraid_capture)
    MANTINE = (Items.Progression.mantine, True, 0xE, Locations.ShadowPokemon.mantine_capture)
    QWILFISH = (Items.Progression.qwilfish, True, 0xF, Locations.ShadowPokemon.qwilfish_capture)
    MEDITITE = (Items.Progression.meditite, True, 0x10, Locations.ShadowPokemon.meditite_capture)
    DUNSPARCE = (Items.Progression.dunsparce, True, 0x11, Locations.ShadowPokemon.dunsparce_capture)
    SWABLU = (Items.Progression.swablu, True, 0x12, Locations.ShadowPokemon.swablu_capture)
    SUDOWOODO = (Items.Progression.sudowoodo, True, 0x13, Locations.ShadowPokemon.sudowoodo_capture)
    HITMONTOP = (Items.Progression.hitmontop, True, 0x14, Locations.ShadowPokemon.hitmontop_capture)
    ENTEI = (Items.Progression.entei, True, 0x15, Locations.ShadowPokemon.entei_capture)
    LEDIAN = (Items.Progression.ledian, True, 0x16, Locations.ShadowPokemon.ledian_capture)
    SUICUNE = (Items.Progression.suicune, True, 0x17, Locations.ShadowPokemon.suicune_capture)
    GLIGAR = (Items.Progression.gligar, True, 0x18, Locations.ShadowPokemon.gligar_capture)
    STANTLER = (Items.Progression.stantler, True, 0x19, Locations.ShadowPokemon.stantler_capture)
    PILOSWINE = (Items.Progression.piloswine, True, 0x1A, Locations.ShadowPokemon.piloswine_capture)
    SNEASEL = (Items.Progression.sneasel, True, 0x1B, Locations.ShadowPokemon.sneasel_capture)
    AIPOM = (Items.Progression.aipom, True, 0x1C, Locations.ShadowPokemon.aipom_capture)
    MURKROW = (Items.Progression.murkrow, True, 0x1D, Locations.ShadowPokemon.murkrow_capture)
    FORRETRESS = (Items.Progression.forretress, True, 0x1E, Locations.ShadowPokemon.forretress_capture)
    ARIADOS = (Items.Progression.ariados, True, 0x1F, Locations.ShadowPokemon.ariados_capture)
    GRANBULL = (Items.Progression.granbull, True, 0x20, Locations.ShadowPokemon.granbull_capture)
    VIBRAVA = (Items.Progression.vibrava, True, 0x21, Locations.ShadowPokemon.vibrava_capture)
    RAIKOU = (Items.Progression.raikou, True, 0x22, Locations.ShadowPokemon.raikou_capture)
    SUNFLORA = (Items.Progression.sunflora, True, 0x23, Locations.ShadowPokemon.sunflora_capture)
    DELIBIRD = (Items.Progression.delibird, True, 0x24, Locations.ShadowPokemon.delibird_capture)
    HERACROSS = (Items.Progression.heracross, True, 0x25, Locations.ShadowPokemon.heracross_capture)
    SKARMORY = (Items.Progression.skarmory, True, 0x26, Locations.ShadowPokemon.skarmory_capture)
    MILTANK = (Items.Progression.miltank, True, 0x27, Locations.ShadowPokemon.miltank_capture)
    ABSOL = (Items.Progression.absol, True, 0x28, Locations.ShadowPokemon.absol_capture)
    HOUNDOOM = (Items.Progression.houndoom, True, 0x29, Locations.ShadowPokemon.houndoom_capture)
    TROPIUS = (Items.Progression.tropius, True, 0x2A, Locations.ShadowPokemon.tropius_capture)
    METAGROSS = (Items.Progression.metagross, True, 0x2B, Locations.ShadowPokemon.metagross_capture)
    TYRANITAR = (Items.Progression.tyranitar, True, 0x2C, Locations.ShadowPokemon.tyranitar_capture)
    SMEARGLE = (Items.Progression.smeargle, True, 0x2D, Locations.ShadowPokemon.smeargle_capture, True)
    URSARING = (Items.Progression.ursaring, True, 0x2E, Locations.ShadowPokemon.ursaring_capture, True)
    SHUCKLE = (Items.Progression.shuckle, True, 0x2F, Locations.ShadowPokemon.shuckle_capture, True)
    TOGETIC = (Items.Progression.togetic, True, 0x30, Locations.ShadowPokemon.togetic_capture, True)

    def __init__(self, pokemon_name: str, is_shadow: bool, shadow_id: int, static_location_name: str, is_extra : bool = False) -> None:
        self.pokemon_name : str = pokemon_name
        self.is_shadow: bool = is_shadow
        self.shadow_id : int = shadow_id
        self.static_location_name : str = static_location_name
        self.is_postgame = is_extra

    def get_default_location(self) -> str:
        return self.static_location_name