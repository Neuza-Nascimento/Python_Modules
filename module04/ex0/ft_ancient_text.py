#!/usr/bin/python3

import sys


def cyber_archives_recovery() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        file = None
        print(f"Accessing file: '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            print(f"---\n\n{content}\n\n---")
        except Exception as e:
            print(f"Error opening file {sys.argv[1]}: {e}")
        finally:
            if file:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")


def main() -> None:
    cyber_archives_recovery()


if __name__ == "__main__":
    main()
