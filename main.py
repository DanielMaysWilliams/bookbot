from typing import Any


def main(book_path: str):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = get_letter_counts(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter_count in letter_counts:
        print(f"The '{letter_count["char"]}' character was found {letter_count["count"]} times")
    print("--- End report ---")


def get_num_words(text) -> int:
    words = text.split()
    return len(words)


def get_letter_counts(text: str) -> list[dict[str, Any]]:
    text = text.lower()
    char_counts = {}
    for char in text:
        if not char.isalpha():
            continue
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

    result = []
    for char, count in char_counts.items():
        result.append(
            {
                "char": char,
                "count": count,
            }
        )

    result.sort(reverse=True, key=lambda d: d["count"])
    return result


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    main(book_path)
