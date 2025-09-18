#!/usr/bin/env python3
import sys


def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print("none")
        return

    input_str = args[0]
    z_chars = [c for c in input_str if c == "z"]

    if z_chars:
        print("".join(z_chars))
    else:
        print("none")


if __name__ == "__main__":
    main()
