import pytest
from mindtools import clean_text, word_count, slugify


def test_clean_text():
    assert clean_text("  hello   world  ") == "hello world"


def test_word_count():
    assert word_count("one two three") == 3


def test_text_type_errors():
    with pytest.raises(TypeError):
        clean_text(123)

def test_slugify():
    assert slugify("Hello World From Ghana!") == "hello-world-from-ghana"
    assert slugify("My New Python Library") == "my-new-python-library"
