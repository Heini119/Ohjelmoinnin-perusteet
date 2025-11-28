########################################################
# Task A10_T1
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

def read_file(filename):
    
    values = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    values.append(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return values


def display_vertically(values):
    
    print("# --- Vertically --- #")
    for value in values:
        print(value)
    print("# --- Vertically --- #")


def display_horizontally(values):
   
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")


def main():
    
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    values = read_file(filename)
    if values is None:
        print("Program ending.")
        return

    display_vertically(values)
    display_horizontally(values)

    print("Program ending.")


if __name__ == "__main__":
    main()
