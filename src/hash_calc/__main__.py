import os
import sys

import argparse

from hash_calc.HashCalc import HashCalc
from hash_calc.Controller import Controller

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file which shall be hashed")
    args = parser.parse_args()

    if(os.path.isfile(args.path)):
        c = Controller()
        h = HashCalc(args.path)
        c.printHeader(args.path, h.md5, h.sha256)
        c.printExecutionTime()
        
    else:
        print("The provided path is not a file!")
        pass 


if __name__ == "__main__":
    sys.exit(main())
