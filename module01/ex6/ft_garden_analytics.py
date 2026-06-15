#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self._name = name.capitalize()
        self._age = 0
        self._height = 0.0
        self._growth = growth
        self.set_height(round(height, 2))
        self.set_age(age)
        self._stats: Plant.Stats = Plant.Stats()

    def grow(self) -> None:
        self._height += self._growth
        self._stats.count_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.count_age()

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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.count_show()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def print_display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age,"
                  f" {self._show_calls} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, color: str, isBloom: bool = False):
        super().__init__(name, height, age, growth)
        self._color = color
        self._isBloom = isBloom

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._isBloom is True:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        if self._isBloom is False:
            self._isBloom = True
            self.grow()
            print(f"[asking the {self._name} to grow and bloom]")

    def age_grow_bloom(self) -> None:
        if self._isBloom is False:
            self._isBloom = True
            self.grow()
            self.age()
            print(f"[make {self._name} to grow, age and to bloom]")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, trunk_diameter: float):
        super().__init__(name, height, age, growth)
        self._diameter = trunk_diameter
        self._shade = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self._diameter}cm wide.")
        self._shade += 1

    def display_shade(self) -> None:
        print(f"{self._shade} shade")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, color: str, seeds: int = 0):
        super().__init__(name, height, age, growth, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def age_grow_bloom(self) -> None:
        super().age_grow_bloom()
        self._seeds = 42


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.print_display()


def ft_garden_analytics() -> None:
    print("=" * 31)
    print("=== Garden statistics  ===")
    print("=" * 31)
    print()
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? ->"
          f"{Plant.is_older_than_a_year(400)}\n")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, 0.1, "red")
    rose.show()
    display_statistics(rose)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 10, 5.0)
    oak.show()
    display_statistics(oak)
    oak.display_shade()
    oak.produce_shade()
    display_statistics(oak)
    oak.display_shade()
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, 20.0, "yellow")
    sunflower.show()
    sunflower.age_grow_bloom()
    sunflower.show()
    display_statistics(sunflower)
    print("\n=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_statistics(anon)


if __name__ == "__main__":
    ft_garden_analytics()
