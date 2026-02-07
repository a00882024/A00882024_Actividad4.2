"""Tests for word counting functions."""

# pylint: disable=missing-function-docstring

import unittest

from src.word_counter import (
    count_words,
    count_words_in_lines,
    get_word_frequencies,
    strip_punctuation,
)


class TestCountWords(unittest.TestCase):
    """Tests for the count_words function."""

    def test_simple_sentence(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_single_word(self):
        self.assertEqual(count_words("hello"), 1)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("hello    world"), 2)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_only_spaces(self):
        self.assertEqual(count_words("   "), 0)

    def test_none(self):
        self.assertEqual(count_words(None), 0)

    def test_sentence_with_punctuation(self):
        self.assertEqual(count_words("hello, world!"), 2)


class TestCountWordsInLines(unittest.TestCase):
    """Tests for the count_words_in_lines function."""

    def test_multiple_lines(self):
        lines = ["hello world", "foo bar baz"]
        self.assertEqual(count_words_in_lines(lines), 5)

    def test_empty_lines(self):
        lines = ["hello", "", "world"]
        self.assertEqual(count_words_in_lines(lines), 2)

    def test_empty_list(self):
        self.assertEqual(count_words_in_lines([]), 0)


class TestStripPunctuation(unittest.TestCase):
    """Tests for the strip_punctuation function."""

    def test_trailing_comma(self):
        self.assertEqual(strip_punctuation("hello,"), "hello")

    def test_trailing_period(self):
        self.assertEqual(strip_punctuation("world."), "world")

    def test_surrounding_quotes(self):
        self.assertEqual(strip_punctuation('"hello"'), "hello")

    def test_no_punctuation(self):
        self.assertEqual(strip_punctuation("hello"), "hello")

    def test_only_punctuation(self):
        self.assertEqual(strip_punctuation("..."), "")


class TestGetWordFrequencies(unittest.TestCase):
    """Tests for the get_word_frequencies function."""

    def test_simple_frequency(self):
        result = get_word_frequencies("hello hello world")
        self.assertEqual(result, {"hello": 2, "world": 1})

    def test_single_word(self):
        result = get_word_frequencies("hello")
        self.assertEqual(result, {"hello": 1})

    def test_empty_string(self):
        result = get_word_frequencies("")
        self.assertEqual(result, {})

    def test_none(self):
        result = get_word_frequencies(None)
        self.assertEqual(result, {})

    def test_with_punctuation(self):
        result = get_word_frequencies("hello, world!")
        self.assertEqual(result, {"hello": 1, "world": 1})


if __name__ == '__main__':
    unittest.main()
