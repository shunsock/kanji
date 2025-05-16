from .kanji_pair_data import KANJI_PAIR_DATA

class KanjiMapper:
    def __init__(self):
        self.old_to_new = {ord(p.old): p.new for p in KANJI_PAIR_DATA}
        self.new_to_old = {ord(p.new): p.old for p in KANJI_PAIR_DATA}

    def convert_to_new(self, text: str) -> str:
        return text.translate(self.old_to_new)

    def convert_to_old(self, text: str) -> str:
        return text.translate(self.new_to_old)
