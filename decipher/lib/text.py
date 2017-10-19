"""Utilities for processing text."""

import re


def clean(text):
    """Remove all punctuation and spaces from text."""
    result = re.sub("[^a-z]+", "", text.lower())
    return result
