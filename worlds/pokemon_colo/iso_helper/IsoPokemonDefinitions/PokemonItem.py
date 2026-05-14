from io import BytesIO

class PokemonItem:
    def __init__(self, entry: BytesIO, item_id: int):
        self.entry = entry
        self.item_id = item_id
        self.item_start_byte = 0x360CE8+(0x28*item_id)

    def change_pocket(self, new_pocket: int) -> None:
        self.entry.seek(self.item_start_byte)
        self.entry.write(new_pocket.to_bytes())