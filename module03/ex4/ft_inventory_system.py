#!/usr/bin/python3

import sys

def split_args(arg: str) -> tuple:
    args = arg.split(":")
    if len(args) != 2:
        raise ValueError(f"Error - invalid parameter '{arg}'")
    else:
        key = str(args[0])
        value = int(args[1])
    return key, int(value)


def analise_args() -> dict:
        inventory = {}
        for i in sys.argv[1:]:
            try:
                key, value = split_args(i)
                if key in inventory:
                    print(f"Redundant item '{key}' - discarding")
                else:
                    inventory[key] = value 
            except ValueError as e:
                print(f"Quantity error for 'key':{e}")
        return inventory
            

def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory : dict = analise_args()
    print(f"Got inventory: {inventory}")
    typesInventory : list = list(inventory.keys())
    print(f"Item list: {typesInventory}")
    print(f"Total quantity of the {len(typesInventory)}"
          f"items: {sum(inventory.values())}")
    for i in typesInventory:
        total = inventory[i] / sum(inventory.values()) * 100
        print(f"Item {i} represents {round(total, 1)}%")
    camp : str =  typesInventory[0]
    over : str = typesInventory[0]
    for name in typesInventory:
        if inventory[name] > inventory[camp]:
            camp = name
        elif inventory[name] < inventory[over]:
            over = name
    print(f"Item most abundant: {camp} with quantity {inventory[camp]}")
    print(f"Item least abundant: {over} with quantity {inventory[over]}")
    inventory.update({"magic item": 1})
    print(f"Update inventory: {inventory}")


if __name__ == "__main__":
    main()
