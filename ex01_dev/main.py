#!/usr/bin/env python3

from checkmate import checkmate

import sys

args = sys.argv[1:]


def main():
    if len(args) == 0:
        print("Usage: python main.py <board_file>")
        return

    for file_path in args:
        try:
            with open(file_path, "r") as file:
                board = file.read().strip()
                checkmate(board)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            continue

if __name__ == "__main__":
    main()
