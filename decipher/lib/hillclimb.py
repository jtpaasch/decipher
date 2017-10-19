"""Hill climb/steepest ascent utilities."""

from heapq import nlargest
from random import choice

from . import analysis
from . import keys
from . import decrypt


def get_next_key(
        n, key, ciphertext, score,
        probabilities, default_probability):
    """Search through swapped keys for the best scoring key."""
    for i, j in keys.get_swaps():
        next_key = keys.get_swapped_key(key, i, j)
        plaintext = decrypt.decrypt(next_key, ciphertext)
        next_score = analysis.get_fitness(
            n, plaintext, probabilities, default_probability)
        if next_score > score:
            yield next_score, next_key


def select_fittest(candidates):
    """Pick a key out of the 10 best candidate keys."""
    result = None
    fittest_candidates = nlargest(10, candidates, key=lambda x: x[0])
    if fittest_candidates:
        result = choice(fittest_candidates)
    return result


def search(
        log, n, best_key, ciphertext, best_score,
        probabilities, default_probability):
    """Search via hill climb/ascent for best key."""
    candidate = (best_score, best_key)
    while candidate:
        candidates = [(score, key) for score, key in get_next_key(
                      n, best_key, ciphertext, best_score,
                      probabilities, default_probability)]
        candidate = select_fittest(candidates)
        if candidate:
            best_score, best_key = candidate[0], candidate[1]
            log("{}: {}".format(best_score, best_key))

    return best_score, "".join(best_key)
