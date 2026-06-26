#!/usr/bin/python3


def secure_archive(name_file: str, op: str = "r", content: str = ""
                   ) -> tuple[bool, str]:
    try:
        if (op == "r"):
            with open(name_file, "r") as file:
                return (True, file.read())
        else:
            with open(name_file, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = (secure_archive("teste"))
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("text", "w", result[1]))


if __name__ == "__main__":
    main()
