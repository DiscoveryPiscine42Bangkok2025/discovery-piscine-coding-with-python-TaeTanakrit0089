#!/usr/bin/env python3
import sys


def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print("none")
        return

    user_input = input("What was the parameter? ")

    if user_input == args[0]:
        print("Good job!")
    else:
        print("Nope, sorry...")


if __name__ == "__main__":
    main()
