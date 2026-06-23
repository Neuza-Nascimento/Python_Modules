#!/usr/bin/python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    n = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    if n >= 2:
        print(f"Arguments received: {n - 1}")
        i = 1
        while i < n:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {n} ")


if __name__ == "__main__":
    main()
