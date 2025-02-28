from typing import Any


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
