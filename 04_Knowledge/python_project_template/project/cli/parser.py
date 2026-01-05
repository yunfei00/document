from __future__ import annotations

import argparse
from pathlib import Path

from .commands import train, eval, init_workdir

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="project", description="Project CLI")

    parser.add_argument("-v", "--verbose", action="count", default=0, help="verbosity (-v/-vv)")
    parser.add_argument("--workdir", type=Path, default=Path("./workdir"), help="work directory")

    sub = parser.add_subparsers(dest="command", required=True)

    train.register(sub)
    eval.register(sub)
    init_workdir.register(sub)

    return parser
