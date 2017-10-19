"""Unit tests for the ``lib.analysis`` module."""

from unittest import TestCase

from decipher.lib import analysis


class TestAnalysis(TestCase):
    """Test suite for the ``lib.analysis`` module."""

    def test_num_ngrams(self):
        """Ensure ``num_ngrams()`` counts ngrams correctly."""
        result = analysis.num_ngrams(3, 'abcd')
        self.assertEqual(result, 2)

    def test_ngrams(self):
        """Ensure ``ngrams()`` yields ngrams correctly."""
        result = [ngram for ngram in analysis.ngrams(3, 'abcd')]
        self.assertEqual(result, ['abc', 'bcd'])
