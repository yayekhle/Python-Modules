import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, qty = arg.split(":", 1)
        item, qty = item.strip(), qty.strip()
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            inventory[item] = int(qty)
        except ValueError:
            print(f"Quantity error for '{item}': invalid literal for int()"
                  f" with base 10: '{qty}'")
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for item, qty in inventory.items():
        percent = (qty / total) * 100 if total else 0
        print(f"Item {item} represents {round(percent, 1)}%")

    if inventory:
        max_item = max(inventory, key=inventory.get)
        min_item = min(inventory, key=inventory.get)
        print(f"Item most abundant: {max_item} "
              f"with quantity {inventory[max_item]}")
        print(f"Item least abundant: {min_item} "
              f"with quantity {inventory[min_item]}")

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
