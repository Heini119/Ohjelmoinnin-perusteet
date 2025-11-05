def main():
    print("Program starting.")

    line1 = input("Insert first name: ")
    line2 = input("Insert last name: ")

    feed = input("Insert filename: ")
    
    file = open(feed, "w")
    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write("\n")
    file.close()

    print("Program ending.")
if __name__ == "__main__":
    main()