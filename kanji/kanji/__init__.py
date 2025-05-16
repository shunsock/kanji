from .kanji_pair_mapper import (
    replace_new_to_old,
    replace_old_to_new,
)
from .kanji_pair import KanjiPair
from .kanji_pair_data import (
    KANJI_NEW_TO_OLD,
    KANJI_OLD_TO_NEW,
    KANJI_PAIRS,
)

__all__ = [
    "KANJI_NEW_TO_OLD",
    "KANJI_OLD_TO_NEW",
    "KANJI_PAIRS",
    "KanjiPair",
    "replace_new_to_old",
    "replace_old_to_new",
]
