import sys


def main():
    print("=== Player Score Analytics ===")
    args = sys.argv
    valid = []
    for x in range(1, len(args)):
        try:
            valid.append(int(args[x]))
        except ValueError:
            print(f"Invalid Parameter : '{args[x]}'")
    print()
    if (len(valid) == 0):
        print("No scores provided.")
    else:
        print("Scores processed:", valid)
        print("Total players:", len(valid))
        print("Total score:", sum(valid))
        print("Average score:", sum(valid) / len(valid))
        print("Highest score:", max(valid))
        print("Lowest score:", min(valid))
        print("Score range:", max(valid) - min(valid))


if __name__ == "__main__":
    main()
