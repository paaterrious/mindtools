# MindTools

A small, beginner-friendly Python library containing practical utilities that can be reused across projects.

## Features

- Text cleaning and word counting
- Safe nested dictionary access
- File size formatting
- Simple retry helper
- Easy-to-understand source code
- Unit tests included
- Ready for GitHub and PyPI packaging

## Project structure

```text
mindtools/
├── src/
│   └── mindtools/
│       ├── __init__.py
│       ├── text.py
│       ├── data.py
│       ├── files.py
│       └── retry.py
├── tests/
│   ├── test_text.py
│   ├── test_data.py
│   ├── test_files.py
│   └── test_retry.py
├── examples/
│   └── basic_usage.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Installation for development

Open the project folder in VS Code, create a virtual environment, and install it in editable mode:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Then:

```bash
python -m pip install --upgrade pip
pip install -e .
```

Install the test dependency:

```bash
pip install pytest
```

Run the tests:

```bash
pytest
```

## Example

```python
from mindtools import clean_text, word_count, get_nested, format_bytes

text = "   Hello,   Python world!   "

print(clean_text(text))
print(word_count(text))

data = {"user": {"profile": {"name": "Alex"}}}
print(get_nested(data, "user.profile.name"))

print(format_bytes(1024 * 1024))
```

## GitHub

After creating a repository named `mindtools` on GitHub:

```bash
git init
git add .
git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mindtools.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## License

MIT License. See `LICENSE`.
