import os
from typing import Literal
from obsidian_query.src.chat_engine import ObsidianEngine
from llama_index.readers.obsidian.base import ObsidianReader
from llama_index.core import VectorStoreIndex
def menu() -> int:
    op = 0
    while op not in [1, 2, 3]:
        os.system("clear") if os.name == "posix" else os.system("cls")
        print("--- Obsidian Query ---\n")
        print("1. Query vault")
        print("2. Regenerate vector store index")
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
            query = input("Enter query:\n>>")

            engine = ObsidianEngine(
                retriever=ObsidianReader(
                    input_dir=""
                ).load_data()
            )
        case 2:
            pass
        case 3:
            exit()


if __name__ == "__main__":
    main()
