import pytest
from utils import count_vowels


@pytest.mark.parametrize("text, expected", [
    ("Python", 2),           # y, o
    ("AEIOUY", 6),           # A, E, I, O, U, Y
    ("bcd", 0),              # brak
    ("", 0),                 # brak
    ("Próba żółwia", 5),     # ó, a, ó, i, a (zmienione z 4 na 5)
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
