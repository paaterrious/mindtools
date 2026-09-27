from mindtools import clean_text, word_count, get_nested, format_bytes


def main():
    text = "   Hello,    Python   library!   "

    print("Cleaned:", clean_text(text))
    print("Words:", word_count(text))

    user = {
        "profile": {
            "name": "Alex",
            "role": "Developer",
        }
    }

    print("Name:", get_nested(user, "profile.name"))
    print("Missing:", get_nested(user, "profile.email", "Not found"))

    print("File size:", format_bytes(5 * 1024 * 1024))


if __name__ == "__main__":
    main()
