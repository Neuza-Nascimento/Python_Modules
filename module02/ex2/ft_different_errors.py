#!/usr/bin/python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abs" + 2


def test_error_types() -> None:
    for i in range(0, 5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")
        except TypeError as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")
    print("\nAll error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()


if __name__ == "__main__":
    main()
