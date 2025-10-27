"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re


def count_characters(text):
    """Count non-space characters in a string."""
    return sum(1 for ch in text if not ch.isspace())


def count_words(text):
    """Count number of words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    matches = re.findall(r"-?\d+", text)
    return [int(m) for m in matches]


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = (total / len(numbers)) if numbers else None
    return {
        "characters": chars,
        "words": words,
        "numbers": numbers,
        "sum": total,
        "average": average,
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    result = analyze_text(text)
    print(f"Non-space characters: {result['characters']}")
    print(f"Word count: {result['words']}")
    print(f"Numbers found: {result['numbers']}")
    print(f"Sum of numbers: {result['sum']}")
    avg = result["average"]
    print(
        f"Average of numbers: {avg:.2f}"
        if avg is not None
        else "Average of numbers: N/A"
    )
