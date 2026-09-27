def format_bytes(size: int) -> str:
    """Convert a byte count into a human-readable string.

    Examples:
        0 -> "0 B"
        1024 -> "1.00 KB"
        1048576 -> "1.00 MB"
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size cannot be negative")

    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} B"
            return f"{value:.2f} {unit}"
        value /= 1024

    return f"{value:.2f} PB"
