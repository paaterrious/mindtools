_MISSING = object()


def get_nested(data: dict, path: str, default=None):
    """Read a nested dictionary value using dot notation.

    Example:
        get_nested({"user": {"name": "Sam"}}, "user.name")
        -> "Sam"

    If the path does not exist, ``default`` is returned.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    if not isinstance(path, str) or not path:
        raise ValueError("path must be a non-empty string")

    current = data

    for key in path.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current
