"""Logging utilities."""

import logging
import sys


def get_logger():
    """Get a stdout logger."""
    name = "main-log"
    fmt = "%(message)s"
    formatter = logging.Formatter(fmt)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    log = logging.getLogger(name)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log


def make_writer(log_func):
    """Generate a function you can send messages to."""
    def inner_func(msg):
        result = "-- {}".format(msg)
        log_func(result)
    return inner_func


def get_log(is_verbose):
    """Get a callable we can send messages to."""
    log = get_logger()
    return make_writer(log.info) if is_verbose else lambda x: None
