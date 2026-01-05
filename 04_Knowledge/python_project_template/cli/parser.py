import argparse
def build_parser():
    p = argparse.ArgumentParser(prog="project")
    p.add_argument("-v", action="count", default=0)
    sub = p.add_subparsers(required=True)
    return p
