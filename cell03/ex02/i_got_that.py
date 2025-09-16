#!/usr/bin/env python3

def main():
    user_input = input("What you gotta say? : ")
    while user_input != "STOP":
        print("I got that! Anything else? :", end=" ")
        user_input = input()

if __name__ == "__main__":
    main()
