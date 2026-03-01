import pytest
from lib.palindrome import longest_palindromic_substring


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_same_characters():
    assert longest_palindromic_substring("aa") == "aa"


def test_two_different_characters():
    assert longest_palindromic_substring("ab") in ["a", "b"]


def test_odd_length_example():
    # babad can validly return "bab" or "aba"
    assert longest_palindromic_substring("babad") in ["bab", "aba"]


def test_even_length_example():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_entire_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_long_palindrome_in_middle():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"


def test_no_longer_than_one():
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]