#!/usr/bin/python3

import sys


def cyber_archives_recovery() -> str:
    if len(sys.argv) != 2:
        sys.stderr.write(f"\n[STDERR] Usage: {sys.argv[0]} <file>\n")
    else:
        file = None
        sys.stdout.write(f"\nAccessing file: '{sys.argv[1]}'\n")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            sys.stdout.write(f"---\n\n{content}\n\n---")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
            return None
        finally:
            if file:
                file.close()
                sys.stdout.write(f"\nFile '{sys.argv[1]}' closed.\n")
        return content


def cyber_archives_recovery_preservation() -> None:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    content = cyber_archives_recovery()
    if content:
        content_new_line = [line + "#" for line in content.splitlines()]
        content = "\n".join(content_new_line)
        sys.stdout.write("\nTransform data:\n")
        sys.stdout.write(f"---\n\n{content}\n\n---")
        sys.stdout.write("Enter new file name (or empty):")
        sys.stdout.flush()
        name_file = sys.stdin.readline().strip()
        if not name_file:
            sys.stdout.write("Not saving data.\n")
            return
        try:
            sys.stdout.write(f"Saving data to '{name_file}'\n")
            file = open(name_file, "w")
            file.write(content)
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
            sys.stdout.write("Not saving data.\n")
            return
        sys.stdout.write(f"Data saved in file {name_file}\n")

    

def main() -> None:
    cyber_archives_recovery_preservation()

if __name__== "__main__":
    main()