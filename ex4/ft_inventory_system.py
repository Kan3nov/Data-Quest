import sys


def main():
    args = sys.argv
    inventory = {}
    print("=== Inventory System Analysis ===")
    if len(args) == 1:
        print("No arguments were provided - exiting")
        return
    for x in range(1, len(args)):
        item = args[x]
        try:
            key, value = item.split(":")
        except Exception:
            print(f"Error - invalid parameter '{item}'")
        else:
            try:
                if (key in inventory.keys()):
                    print(f"Redundant item '{key}' - discarding")
                    continue
                inventory[key] = int(value)
            except ValueError as e:
                print(f"Quantity error for '{key}':", e)
    print()
    print("Got inventory :", inventory)

    print("Item list: [", ", ".join(inventory.keys()), "]", sep='')

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.keys())}" +
          f" items: {total_quantity}")

    for key, value in inventory.items():
        max_key = key
        max_value = value
        break
    for key, value in inventory.items():
        if value > max_value:
            max_key = key
            max_value = value
    print("Item most abundant:", max_key, "with quantity", max_value)

    for key, value in inventory.items():
        min_key = key
        min_value = value
        break
    for key, value in inventory.items():
        if value < min_value:
            min_key = key
            min_value = value
    print("Item least abundant: ", min_key, "with with quantity", min_value)

    for key, value in inventory.items():
        print(f"Item {key} represents ",
              round(value / total_quantity * 100, 1),
              "%", sep="")

    inventory["magic_item"] = 1
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
