from __future__ import annotations
import logging

logger = logging.getLogger(__name__)

def register(subparsers):
    p = subparsers.add_parser("eval", help="evaluate")
    p.add_argument("--ckpt", required=True)
    p.set_defaults(func=run)

def run(args):
    logger.info("eval ckpt=%s workdir=%s", args.ckpt, args.workdir)
