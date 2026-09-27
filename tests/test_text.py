import pytest
from mindtools import clean_text, word_count


def test_clean_text():
    assert clean_text("  hello   world  ") == "hello world"


def test_word_count():
    assert word_count("one two three") == 3


def test_text_type_errors():
    with pytest.raises(TypeError):
        clean_text(123)
