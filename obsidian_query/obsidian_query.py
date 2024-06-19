import os
from typing import Literal
from src.query_engine import QueryEngine


def menu() -> int:
    op = 0
    while op not in [1, 2, 3]:
        os.system("clear") if os.name == "posix" else os.system("cls")
        print("--- Obsidian Query ---\n")
        print("1. Query vault")
        print("2. Settings")
        print("3. Exit")
        try:
            op = int(input("Enter option:\n>>"))
        except ValueError:
            print("Invalid option. Please try again.")
    return op


def settings():
    print("Settings")


def main():
    op = menu()
    match op:
        case 1:
            pass
        case 2:
            pass
        case 3:
            exit()


if __name__ == "__main__":
    main()
