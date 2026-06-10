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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str , height: float, age: int, 
                 color: str, isBloom: bool = False):
        super().__init__(name, height, age)
        self._color = color
        self._isBloom = isBloom

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._isBloom is True:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
        
    def bloom(self):
        if self._isBloom is False:
            self._isBloom = True
            print(f"[asking the {self._name} to bloom]")


class Tree(Plant):
    def __init__(self, name: str , height: float, age: int, 
                 trunk_diameter : float):
        super().__init__(name, height, age)
        self._diameter = trunk_diameter 

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._diameter}")
    
    def produce_shade(self):
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}", end=" ")
        print(f"long and {self._diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str , height: float, age: int, 
                 nutritional_value: float, harvest_season: str ):
        super().__init__(name, height, age)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")

    def grow(self):
        self._nutritional_value =+1

    def age(self):
        self._nutritional_value =+1
      

def ft_garden_security() -> None:
    print("=" * 31)
    print("=== Garden Security System  ===")
    print("=" * 31)



if __name__ == "__main__":
    ft_garden_security()
