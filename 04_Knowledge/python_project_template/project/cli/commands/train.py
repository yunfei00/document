from __future__ import annotations
import logging

logger = logging.getLogger(__name__)

def register(subparsers):
    p = subparsers.add_parser("train", help="train a model")
    p.add_argument("--epochs", type=int, default=50)
    p.add_argument("--lr", type=float, default=1e-3)
    p.set_defaults(func=run)

def run(args):
    logger.info("training start epochs=%s lr=%s workdir=%s", args.epochs, args.lr, args.workdir)
