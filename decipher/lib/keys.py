"""Utilities for working with cipher/decryption keys."""

from itertools import combinations
from random import shuffle

from . import constants


def get_swaps():
    """Yield all combinations of 2-letters in the alphabet."""
    num_letters = len(constants.ALPHABET)
    combos = combinations(range(num_letters), 2)
    swaps = list(combos)
    for swap in swaps:
        yield swap


def get_swapped_key(key, i, j):
    """Swap two letters in a key."""
    result = list(key)
    result[i], result[j] = result[j], result[i]
    return "".join(result)


def randomize_key(key):
    """Shuffle a key."""
    letters = list(key)
    shuffle(letters)
    return "".join(letters)
