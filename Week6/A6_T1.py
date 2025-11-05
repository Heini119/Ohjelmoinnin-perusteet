def main():
    print("Program starting.")
    print("This program can read a file.")

    filename = input("Insert filename: ")

    print(f'#### START "{filename}" ####')
    print(open(filename).read())
    print(f'#### END "{filename}" ####')

    print("Program ending.")

if __name__ == "__main__":
    main()


