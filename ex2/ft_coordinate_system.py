import math


def get_player_pos() -> tuple:
    while True:
        try:
            coord_str = input("Enter the coordinates in format 'x y z': ")\
                        .split()
            coord = [0.0] * len(coord_str)
            for x in range(len(coord_str)):
                coord[x] = float(coord_str[x])
            if (len(coord) != 3):
                print("3 values are required only!")
                continue
        except ValueError:
            print("Invalid input, only real numbers are permitted")
        else:
            break
    return tuple(coord)


def compute_distance(p1: tuple, p2: tuple) -> float:
    x_diff = (p1[0] - p2[0]) ** 2
    y_diff = (p1[1] - p2[1]) ** 2
    z_diff = (p1[2] - p2[2]) ** 2
    return math.sqrt(x_diff + y_diff + z_diff)


def main():
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    coords = get_player_pos()
    print("Got a first tuple:", coords)
    print(f"It includes: X:{coords[0]}, Y={coords[1]}, Z={coords[2]}")
    print("distance to center:", round(compute_distance(coords, (0, 0, 0)), 2))
    print()
    print("Get a second set of coordinates")
    coords2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          round(compute_distance(coords, coords2), 2))


if __name__ == "__main__":
    main()
