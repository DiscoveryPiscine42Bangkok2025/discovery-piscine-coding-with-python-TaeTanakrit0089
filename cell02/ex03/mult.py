#!/usr/bin/env python3

first = int(input())
second = int(input())

result = first * second

print(f"{first} x {second} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

