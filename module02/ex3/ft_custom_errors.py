#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def ft_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def ft_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        ft_plant_error()
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("\nTesting WaterError...")
    try:
        ft_water_error()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("\nTesting catching all garden errors...")
    errors = [
        ft_plant_error,
        ft_water_error,
    ]
    for error in errors:
        try:
            error()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    main()
