import re


def clean_text(text: str) -> str:
    """Normalize whitespace and trim a string.

    Args:
        text: Text to clean.

    Returns:
        The cleaned text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return re.sub(r"\s+", " ", text).strip()


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return len(text.split())

def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
    return text.strip("-")
