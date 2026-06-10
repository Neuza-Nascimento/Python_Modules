#!/usr/bin/python3

def garden_intro() -> None:
    plant: str = "Rose"
    age: int = 30
    height: int = 25

    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    garden_intro()
