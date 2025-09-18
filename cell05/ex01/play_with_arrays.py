#!/usr/bin/env python3

def main():
    # Define the original array
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # Build the new array by adding 2 to each element
    new_array = [x + 2 for x in original_array]

    # Display both arrays
    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")


if __name__ == "__main__":
    main()
