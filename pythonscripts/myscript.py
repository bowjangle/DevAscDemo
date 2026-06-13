
"""myscript.py

Simple scaffolded Python script.

Usage:
	python myscript.py --name Alice
"""
from __future__ import annotations

import argparse
import logging
import sys

__version__ = "0.1.0"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="A simple scaffolded script.")
	parser.add_argument("--name", "-n", help="Name to greet", default="World")
	parser.add_argument("--verbose", "-v", help="Enable verbose logging", action="store_true")
	parser.add_argument("--version", action="version", version=__version__)
	return parser.parse_args(argv)


def setup_logging(verbose: bool) -> None:
	level = logging.DEBUG if verbose else logging.INFO
	logging.basicConfig(level=level, format="%(asctime)s %(levelname)s: %(message)s")


def greet(name: str) -> str:
	msg = f"Hello, {name}!"
	logging.info("Prepared greeting for %s", name)
	return msg


def main(argv: list[str] | None = None) -> int:
	args = parse_args(argv)
	setup_logging(args.verbose)
	greeting = greet(args.name)
	print(greeting)
	return 0


if __name__ == "__main__":
	raise SystemExit(main(sys.argv[1:]))

print("hello sista!")
