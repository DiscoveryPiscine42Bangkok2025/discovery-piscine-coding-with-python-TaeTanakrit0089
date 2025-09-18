#!/usr/bin/env python3
import sys


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print("none")
        return

    try:
        start = int(args[0])
        end = int(args[1])
    except ValueError:
        print("none")
        return

    # inclusive range, so add +1
    values = list(range(start, end + 1))
    print(values)


if __name__ == "__main__":
    main()
