#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._age = 0
        self._height = 0.0
        self.set_height(round(height, 2))
        self.set_age(age)
        if self._age == age and self._height == height:
            print("Plant created:", end=" ")
            print(f"{self._name}: {self._height}cm, {self._age} days old\n")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def update_height(self, height: float) -> None:
        self.set_height(height)
        if self._height == height:
            print(f"Height updated: {height}cm")

    def update_age(self, age: int) -> None:
        self.set_age(age)
        if self._age == age:
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def info(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


def ft_garden_security() -> None:
    print("=" * 31)
    print("=== Garden Security System  ===")
    print("=" * 31)
    rose = Plant("Rose", 25.0, 30)
    rose.update_height(25.5)
    rose.update_age(50)
    print()
    rose.update_age(-10)
    rose.update_height(-24)
    print(f"\nCurrent state: {rose.info()}")


if __name__ == "__main__":
    ft_garden_security()
