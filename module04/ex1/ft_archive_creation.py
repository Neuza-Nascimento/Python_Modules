#!/usr/bin/python3

import sys


def cyber_archives_recovery() -> str | None:
    content = None
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        file = None
        print(f"Accessing file: '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            print(f"---\n\n{content}\n\n---")
        except Exception as e:
            print(f"Error opening file '': {e}")
        finally:
            if file:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")
    return content


def save_file(content: str) -> None:
    name_file = str(input("Enter new file name (or empty): "))
    if not name_file:
        print("Not saving data.")
        return
    try:
        print(f"Saving data to '{name_file}'")
        file = open(name_file, "w")
        file.write(content)
        print(f"Data saved in file {name_file}")
    except Exception as e:
        print(f"Error opening file: {e}")


def cyber_archives_recovery_preservation() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    content = cyber_archives_recovery()
    if not content:
        return
    content_new_line = [line + "#" for line in content.splitlines()]
    content = "\n".join(content_new_line)
    print("\nTransform data:")
    print(f"---\n\n{content}\n\n---")
    save_file(content)


def main() -> None:
    cyber_archives_recovery_preservation()


if __name__ == "__main__":
    main()
