def main():
    print("Program satarting.")
    print("This program analyses a list of names from a file.")

    file = input("Insert filename to read: ")
    print(f"Reading names from {file}.")
    file = open(file, 'r')
    names = file.readlines()

    print("Program ending.")
if __name__ == "__main__":
    main()