def main():
    print("Program starting.")
    print("This program can copy a file.")

    sfile = input("Insert source filename:")
    dfile = input("Insert destination filename:")

    print(f"Reading file {sfile} content.")

    file = open(sfile, 'r')
    lines = file.readlines()

    print("File content ready in memory.")
    print(f"Writing content into file {dfile}.")

    file = open(dfile, 'w')
    file.writelines(lines)

    print("Copying operation complete.")

    print("Program ending.")

if __name__ == "__main__":
    main()