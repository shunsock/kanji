from .kanji_pair_data import KANJI_OLD_TO_NEW, KANJI_NEW_TO_OLD

def replace_old_to_new(text: str) -> str:
    return text.translate(KANJI_OLD_TO_NEW)

def replace_new_to_old(text: str) -> str:
    return text.translate(KANJI_NEW_TO_OLD)
