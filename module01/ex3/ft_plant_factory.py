#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.heigth = round(height, 2)
        self.age = age

    def show(self):
        print(f"Created: {self.name}: {self.heigth}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Garden Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Sunflower", 80.0, 45),
        Plant("Cactus", 15.0, 120),
        Plant("Tulip", 50.0, 90),
        Plant("Fern", 5.0, 120),
    ]
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
