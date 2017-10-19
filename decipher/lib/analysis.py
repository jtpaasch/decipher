"""Tools for doing n-gram analysis."""

import math

from collections import Counter


def num_ngrams(n, text):
    """Return the number of ngrams in some text."""
    return (len(text) - n) + 1


def ngrams(n, text):
    """Yield ngrams from some text."""
    for i in range(num_ngrams(n, text)):
        yield text[i:i+n]


def get_counts_and_total(n, corpus):
    """Get counts and total for all ngrams in a corpus."""
    counts = Counter(ngrams(n, corpus))
    total = num_ngrams(n, corpus)
    return (counts, total)


def get_probabilities(counts, total):
    """Get a dictionary of probabilities of ngrams in a language."""
    result = {}
    for ngram, count in counts.items():
        result[ngram] = math.log(count / total)
    return result


def get_fitness(n, plaintext, probabilities, default_probability):
    """Sum the natural log probability of all ngrams in some text."""
    result = []
    for ngram in ngrams(n, plaintext):
        ngram_probability = probabilities.get(ngram, default_probability)
        result.append(ngram_probability)
    return sum(result)
