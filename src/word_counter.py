"""Word counting functions implementation."""

PUNCTUATION = '.,;:!?()[]{}"\'-'


def strip_punctuation(word):
    """
    Strip punctuation from a word.

    Args:
        word: String to strip punctuation from

    Returns:
        Word without leading/trailing punctuation
    """
    result = ''
    for char in word:
        if char not in PUNCTUATION:
            result += char
    return result


def count_words(text):
    """
    Count words in a text using naive space splitting.

    Args:
        text: String to count words in

    Returns:
        Number of words
    """
    if not text or not text.strip():
        return 0

    words = text.split()
    return len(words)


def count_words_in_lines(lines):
    """
    Count words across multiple lines.

    Args:
        lines: List of strings

    Returns:
        Total word count
    """
    total = 0
    for line in lines:
        total += count_words(line)
    return total


def get_word_frequencies(text):
    """
    Get frequency of each word in text.

    Args:
        text: String to analyze

    Returns:
        Dictionary of word frequencies
    """
    if not text or not text.strip():
        return {}

    words = text.split()
    frequencies = {}

    for word in words:
        clean_word = strip_punctuation(word)
        if clean_word:
            frequencies[clean_word] = frequencies.get(clean_word, 0) + 1

    return frequencies
