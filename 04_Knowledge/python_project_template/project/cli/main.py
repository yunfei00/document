from __future__ import annotations

from .parser import build_parser
from .logging_setup import setup_logging

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    setup_logging(args.verbose)
    args.func(args)

if __name__ == "__main__":
    main()
