#!/usr/bin/python3

import sys

def cyber_archives_recovery() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        file = None
        print(f"Accessing file: '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            print("---\n")
            print(content)
            print("\n---")
        except Exception as e:
            print(f"Error opening file '': {e}")
        finally:
            if file:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")
    

def main() -> None:
    cyber_archives_recovery()

if __name__== "__main__":
    main()