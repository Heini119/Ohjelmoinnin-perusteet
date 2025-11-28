########################################################
# Task A9_T3
# Developer Heini Käräjämäki
# Date 2025-11-27
########################################################

import sys

def ask_filename():
    return input("Insert filename: ")

def print_file_header(filename):
    print("## " + filename + " ##")

def print_file_content(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Couldn't read file '{filename}'.")
        sys.exit(1)

def main() -> None:

    print("Program starting.")

    filename = ask_filename()

    print_file_header(filename)
    print_file_content(filename)
    print_file_header(filename)


    print("Program ending.")

if __name__ == "__main__":
    main()