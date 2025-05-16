from dataclasses import dataclass

@dataclass(frozen=True)
class KanjiPair:
    old: str
    new: str

    def __post_init__(self):
        if len(self.old) != 1 or len(self.new) != 1:
            raise ValueError("Both kanji characters must be single characters.")
        if self.old == self.new:
            raise ValueError("Old and new kanji characters must be different.")

