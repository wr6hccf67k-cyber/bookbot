def get_book_words(book: str) -> str:
    return f"Found {len(book.split())} total words"


def get_count_characters(book: str) -> dict[str, int]:
    record_characters = {}
    for char in book:
        if char.lower() not in record_characters:
            record_characters[char.lower()] = 0
        record_characters[char.lower()] = record_characters[char.lower()] + 1
    return record_characters


def sort_on(value: tuple[str, int]) -> int:
    return value[1]


def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str, int]]:
    values = []
    for c in chars:
        container = (c, chars[c])
        values.append(container)
    return sorted(values, reverse=True, key=sort_on)
