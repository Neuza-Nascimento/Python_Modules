#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")

    def grow(self) -> None:
        self._age = self._age + 1

    def age(self) -> None:
        self.height = self.height + self.growth

    def age_and_grow(self) -> None:
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.age()
            self.grow()
            print(f"{self.name}: {round(self.height, 2)}cm,", end=" ")
            print(f"{self._age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    frist = rose.height
    rose.show()
    rose.age_and_grow()
    print(f"Growth this week: {round(rose.height - frist, 2)}cm")


if __name__ == "__main__":
    ft_garden_data()
