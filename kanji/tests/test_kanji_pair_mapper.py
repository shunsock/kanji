from kanji.kanji_pair_mapper import replace_old_to_new, replace_new_to_old


class TestKanjiPairMapper:
    def test_replace_old_to_new(self):
        """Test replacing old kanji with new kanji."""
        # Test with the provided examples
        assert replace_old_to_new("會") == "会"
        assert replace_old_to_new("氣") == "気"

        # Test with multiple kanji in a string
        assert replace_old_to_new("會議氣溫") == "会議気温"

        # Test with mixed kanji and non-kanji characters
        assert (
            replace_old_to_new("今日の會議は氣溫について") == "今日の会議は気温について"
        )

        # Test with no replaceable kanji
        assert replace_old_to_new("こんにちは") == "こんにちは"

        # Test with an empty string
        assert replace_old_to_new("") == ""

    def test_replace_new_to_old(self):
        """Test replacing new kanji with old kanji."""
        # Test with the provided examples
        assert replace_new_to_old("会") == "會"
        assert replace_new_to_old("気") == "氣"

        # Test with multiple kanji in a string
        assert replace_new_to_old("会議気温") == "會議氣溫"

        # Test with mixed kanji and non-kanji characters
        assert (
            replace_new_to_old("今日の会議は気温について") == "今日の會議は氣溫について"
        )

        # Test with no replaceable kanji
        assert replace_new_to_old("こんにちは") == "こんにちは"

        # Test with an empty string
        assert replace_new_to_old("") == ""

    def test_bidirectional_conversion(self):
        """Test that converting back and forth results in the original text."""
        original_old = "會議氣溫"
        converted_to_new = replace_old_to_new(original_old)
        assert converted_to_new == "会議気温"
        converted_back_to_old = replace_new_to_old(converted_to_new)
        assert converted_back_to_old == original_old

        original_new = "会議気温"
        converted_to_old = replace_new_to_old(original_new)
        assert converted_to_old == "會議氣溫"
        converted_back_to_new = replace_old_to_new(converted_to_old)
        assert converted_back_to_new == original_new
