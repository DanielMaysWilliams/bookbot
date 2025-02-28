import sys

from stats import get_num_words, get_letter_counts


def main(book_path: str):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = get_letter_counts(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter_count in letter_counts:
        print(f"{letter_count['char']}: {letter_count['count']}")
    print("--- End report ---")


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    main(book_path)
