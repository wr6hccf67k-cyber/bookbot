from stats import get_book_words
from stats import get_count_characters
from stats import chars_dict_to_sorted_list
import sys


print("Usage: python3 main.py <path_to_book>")
def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


book_path = sys.argv[1]
book = get_book_text(book_path)

chars = get_count_characters(book)


def print_report(
    book_path_location: str,
    word_count: str,
    sorted_list: list[tuple[str, int]],
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path_location}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for item in sorted_list:
        if item[0].isalpha() is True:
            value = f"{item[0]}: {item[1]}"
            print(value)
    print("============= END ===============")


print_report(book_path, get_book_words(book), chars_dict_to_sorted_list(chars))
