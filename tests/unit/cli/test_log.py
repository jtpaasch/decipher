"""Unit tests for the ``cli.log`` module."""

from unittest import TestCase
from unittest.mock import Mock

import logging

from decipher.cli import log as log_lib


class TestLog(TestCase):
    """Test suite for the ``cli.log`` module."""

    def test_get_logger(self):
        """Ensure ``get_logger()`` gets a stdout logger."""
        result = log_lib.get_logger()
        self.assertTrue(isinstance(result, logging.Logger))

    def test_make_writer(self):
        """Ensure ``make_writer()`` returns a write function."""
        log_func = Mock()
        msg = "dummy-message"
        expected = "-- {}".format(msg)
        writer = log_lib.make_writer(log_func)
        writer(msg)
        log_func.assert_called_once_with(expected)

    def test_get_log(self):
        """Ensure ``get_log()`` returns a callable."""
        result = log_lib.get_log(True)
        self.assertTrue(callable(result))
        result("dummy-message")

        result = log_lib.get_log(False)
        self.assertTrue(callable(result))
        result("dummy-message")
