import sys


def main():
    print("=== Command Quest ===")
    args = sys.argv
    print("Prgram name:", args[0])
    if (len(args) == 1):
        print("No arguments provided!")
    elif (len(args) > 1):
        print("Arguments received:", len(args) - 1)
    for x in range(1, len(args)):
        print(f"Argument {x}: {args[x]}")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
