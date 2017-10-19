"""Decrypting utilities."""

from . import constants


def decrypt(key, ciphertext):
    """Decode ciphertext with a key."""
    return ciphertext.translate(str.maketrans(key, constants.ALPHABET))


def pretty_decrypt(key, ciphertext):
    """Decode ciphertext, with spaces, caps, and punctuation."""
    key_map = zip(list(key), list(constants.ALPHABET))
    trans = dict(key_map)
    result = []
    for char in ciphertext:
        lower_char = char.lower()
        if lower_char in constants.ALPHABET:
            translation = trans.get(lower_char)
            if char.isupper():
                result.append(translation.upper())
            else:
                result.append(translation)
        else:
            result.append(char)
    return "".join(result)
