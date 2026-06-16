#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    plants = [
        'tomato',
        'lettuce',
        'carrots'
    ]
    for plant in plants:
        try:
            water_plant(plant)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
