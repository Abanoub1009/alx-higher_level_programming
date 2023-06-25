#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Retrieve the command-line arguments
    argv = sys.argv[1:]

    # Convert arguments to integers and calculate the sum
    total = sum(int(arg) for arg in argv)

    # Print the result
    print(total)
