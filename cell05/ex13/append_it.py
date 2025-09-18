#!/usr/bin/env python3
import sys


def main():
    args = sys.argv[1:]

    if not args:
        print("none")
        return

    for arg in args:
        if not arg.endswith("ism"):
            print(arg + "ism")


if __name__ == "__main__":
    main()
