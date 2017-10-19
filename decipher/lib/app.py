"""The main module of the app."""

import math
import os

from . import analysis
from . import constants
from . import decrypt
from . import keys
from . import hillclimb
from . import text


def run(log, corpus_file, encoded_file, out_file):
    n = 3
    log("Computing with n = {}".format(n))

    log("Reading corpus file...".format(corpus_file))
    raw_corpus = corpus_file.read()
    corpus = text.clean(raw_corpus)

    log("Computing {}-gram statistics.".format(n))
    counts, total = analysis.get_counts_and_total(n, corpus)
    default_probability = math.log(0.01 / total)
    probabilities = analysis.get_probabilities(counts, total)

    log("Reading encoded ciphertext...".format(encoded_file))
    raw_ciphertext = encoded_file.read()
    ciphertext = text.clean(raw_ciphertext)

    key = keys.randomize_key(constants.ALPHABET)
    log("Starting with random key: {}".format(key))

    plaintext = decrypt.decrypt(key, ciphertext)
    score = analysis.get_fitness(
        n, plaintext, probabilities, default_probability)
    log("Initial plaintext score: {}".format(score))

    log("Beginning hill climb, searching for best key.")
    score, key = hillclimb.search(
        log, n, key, ciphertext, score, probabilities, default_probability)

    log("Finished hill climb.")
    log("--------------------------------------------------------")
    log("Score: " + str(score))
    log("Key: " + str(key))
    log("--------------------------------------------------------")
    log(decrypt.pretty_decrypt(key, raw_ciphertext))
    log("--------------------------------------------------------")

    if score < -5400:
        log("Score is too low. Plaintext is probably deficient.")
        log("Try running the program again.")

    log("")
    log("Writing key to out file.")
    out_file.write("{}{}".format(key, os.linesep))

    log("")
    log("Done.")
