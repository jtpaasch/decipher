Decipher
========

A little program that finds a monoalphabetic substitution key.


Strategy
--------

The program performs a sort of hill-climb/ascent to find a good key. 
It starts with a random key and checks how likely the text it decodes
is to be English. Then it systematically swaps all letters in the key, 
finding swaps that progressively produce text that is more likely 
to be English than before.

The likelihood that decoded text is English is computed by
summing the natural log probabilities of all letter ngrams in the text.
The probabilities for the ngrams are computed from a corpus text.


Installation
------------

Clone the repo somewhere, for instance:

    mkdir -p ~/code
    cd ~/code
    git clone https://github.com/jtpaasch/decipher.git

Create a virtual environment:

    python -m venv venv
    . venv/bin/activate

Install tox:

    pip install tox

And install the package:

    pip install --editable .


Quality
-------

From the root of the repo, run tox:

    tox

This will run the unittests, and print a coverage report.
Only some tests are filled in, as examples.


Run the program
---------------

To execute the program, from the project's repo, with the virtual
environment activated, try this:

    decipherctl --corpus /path/to/corpus-en.txt \
                --infile /path/to/encoded-en.txt \
                --outfile /path/to/key-en.txt \
                --verbose

The program will read the corpus file and the encoded file, it will
find the key, and write it to `/path/to/key-en.txt`. 

If you want to print the key to stdout, specify `--outfile -`, like this:

    decipherctl --corpus /path/to/corpus-en.txt \
                --infile /path/to/encoded-en.txt \
                --outfile - \
                --verbose

If you omit the `--verbose` flag, the program will run without output.
