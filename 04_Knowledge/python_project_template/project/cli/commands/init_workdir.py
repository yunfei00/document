from __future__ import annotations
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def register(subparsers):
    p = subparsers.add_parser("init-workdir", help="initialize workdir structure")
    p.add_argument("--force", action="store_true", help="overwrite existing dirs if needed")
    p.set_defaults(func=run)

def run(args):
    wd: Path = args.workdir
    (wd / "data").mkdir(parents=True, exist_ok=True)
    (wd / "runs").mkdir(parents=True, exist_ok=True)
    (wd / "logs").mkdir(parents=True, exist_ok=True)
    logger.info("workdir initialized at %s", wd)
