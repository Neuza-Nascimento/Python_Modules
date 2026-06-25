#!/usr/bin/python3


def secure_archive(name_file: str, op: str, content: str | None) -> tuple:
    try:
        info = [False, None]
        if (op == "r"):
         with open(name_file, "r") as file:
            info[1] = file.read()
            info[0] = True
        elif (op == "w"):
            with open(name_file, "w") as file:
                file.write(content)
                info[0] = True
                info[1] = content     
    except Exception as e:
        info[0] = False
        info[1] = e
    return info
  

def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("teste", "r"))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("text", "w","Content successfully written to file"))


if __name__ == "__main__":
    main()