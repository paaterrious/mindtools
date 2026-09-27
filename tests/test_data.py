import pytest
from mindtools import get_nested


def test_get_nested():
    data = {"user": {"profile": {"name": "Alex"}}}
    assert get_nested(data, "user.profile.name") == "Alex"


def test_get_nested_default():
    assert get_nested({}, "user.name", "Unknown") == "Unknown"


def test_get_nested_invalid_path():
    with pytest.raises(ValueError):
        get_nested({}, "")
