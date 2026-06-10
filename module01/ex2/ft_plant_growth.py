#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self):
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            print(
                f"{self.name}: {round(self.height, 2)}cm, {self.age} days old")
            self.ager()
            self.grow()

    def grow(self):
        self.age = self.age + 1

    def ager(self):
        self.height = self.height + self.growth


def ft_garden_data() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 5.0, 10, 0.1)
    frist = rose.height
    rose.show()
    print(f"Growth this week: {round(rose.height - frist, 2)}cm")


if __name__ == "__main__":
    ft_garden_data()
