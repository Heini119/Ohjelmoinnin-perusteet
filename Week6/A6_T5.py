SEPARATOR = ";"

def readValues(filename):
    with open(filename, 'r') as file:
        return SEPARATOR.join(line.strip() for line in file)

def analyseValues(values):
    numbers = list(map(int, values.split(SEPARATOR)))
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = round(total / count, 2)
    result = f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n"
    return result

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    result = analyseValues(readValues(filename))
    print(result, end="")
    print("#### Number analysis - END ####")
    print("Program ending.")

if __name__ == "__main__":
    main()

