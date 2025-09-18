#!/usr/bin/env python3

def main():
    num1 = float(input("Give me the first number: "))
    num2 = float(input("Give me the second number: "))

    print("Thank you!")

    print(f"{num1:g} + {num2:g} = {num1 + num2:g}")
    print(f"{num1:g} - {num2:g} = {num1 - num2:g}")
    if num2 != 0:
        print(f"{num1:g} / {num2:g} = {num1 / num2:g}")
    else:
        print(f"{num1:g} / {num2:g} = undefined (division by zero)")
    print(f"{num1:g} * {num2:g} = {num1 * num2:g}")


if __name__ == "__main__":
    main()
