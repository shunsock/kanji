import pytest
from kanji.kanji_pair import KanjiPair


class TestKanjiPair:
    def test_valid_kanji_pair_creation(self):
        """Test that a valid KanjiPair can be created."""
        pair = KanjiPair(old="會", new="会")
        assert pair.old == "會"
        assert pair.new == "会"

    def test_invalid_kanji_pair_length(self):
        """Test that creating a KanjiPair with non-single characters raises ValueError."""
        # Test with old kanji too long
        with pytest.raises(
            ValueError, match="Both kanji characters must be single characters."
        ):
            KanjiPair(old="會會", new="会")

        # Test with new kanji too long
        with pytest.raises(
            ValueError, match="Both kanji characters must be single characters."
        ):
            KanjiPair(old="會", new="会会")

        # Test with both too long
        with pytest.raises(
            ValueError, match="Both kanji characters must be single characters."
        ):
            KanjiPair(old="會會", new="会会")

        # Test with empty strings
        with pytest.raises(
            ValueError, match="Both kanji characters must be single characters."
        ):
            KanjiPair(old="", new="会")

        with pytest.raises(
            ValueError, match="Both kanji characters must be single characters."
        ):
            KanjiPair(old="會", new="")

    def test_same_kanji_pair(self):
        """Test that creating a KanjiPair with identical old and new kanji raises ValueError."""
        with pytest.raises(
            ValueError, match="Old and new kanji characters must be different."
        ):
            KanjiPair(old="会", new="会")
