"""CLI for the package."""

import argparse
import sys

from . import log as cli_log
from ..lib import app


def parse_args(args):
    """Parse command line arguments."""
    desc = "Find a monoalphabetic substitution key and decode."""
    parser = argparse.ArgumentParser(description=desc)

    corp_help = "path to a corpus file"
    parser.add_argument(
        "--corpus", help=corp_help, required=True,
        type=argparse.FileType("r", encoding="UTF-8"))

    infile_help = "path to a file to decode"
    parser.add_argument(
        "--infile", help=infile_help, required=True,
        type=argparse.FileType("r", encoding="UTF-8"))

    outfile_help = "path to write key to"
    parser.add_argument(
        "--outfile", help=outfile_help, required=True,
        type=argparse.FileType("w", encoding="UTF-8"))

    verb_help = "show verbose output?"
    parser.add_argument("--verbose", help=verb_help, action="store_true")

    return parser.parse_args(args)


def cli():
    """Execute/run the CLI."""
    args = parse_args(sys.argv[1:])
    log = cli_log.get_log(args.verbose)
    log("Starting the program...")
    try:
        app.run(log, args.corpus, args.infile, args.outfile)
    except:
        exc_type, exc_val, exc_tb = sys.exc_info()
        msg = "Error - {}: {}".format(exc_type.__name__, exc_val)
        sys.exit(msg)
