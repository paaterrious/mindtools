import pytest
from mindtools import format_bytes


def test_format_bytes():
    assert format_bytes(0) == "0 B"
    assert format_bytes(1024) == "1.00 KB"
    assert format_bytes(1024 * 1024) == "1.00 MB"


def test_negative_bytes():
    with pytest.raises(ValueError):
        format_bytes(-1)
