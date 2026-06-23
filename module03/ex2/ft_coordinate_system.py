#!/usr/bin/python3

import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        input_coordenates = input("Enter new coordinates as "
                                  "floats in format 'x,y,z': ")
        coordenates = input_coordenates.split(",")
        if len(coordenates) != 3:
            print("Invalid syntax")
            continue
        error = False
        params = []
        for coord in coordenates:
            try:
                value = coord.strip()
                params.append(float(value))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")
                error = True
                break
        if error:
            continue
        return params[0], params[1], params[2]


def main() -> None:
    print("Get a first set of coordinates")
    print("=== Game Coordinate System ===")
    pos1 = get_player_pos()
    x, y, z = pos1
    print(f"Got a first tuple: {pos1} ")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    res = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
    print(f"Distance to center: {round(res, 4)}\n")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    final = math.sqrt(((x2 - x) ** 2) + ((y2 - y) ** 2) + ((z2 - z) ** 2))
    print(f"Distance between the 2 sets of coordinates: {round(final, 4)} ")


if __name__ == "__main__":
    main()
