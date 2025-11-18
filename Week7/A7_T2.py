def askIntegers(Values: list[int]) -> None:
    Feed = input("Insert comma separated integers: ")

    for Value in Feed.split(","): #Split the input string into parts
        if Value.isnumeric():
            Values.append(int(Value)) #Convert to integer and add to list
        else:
            print(f"Invalid value '{Value}' detected.")
            continue
    return None

def analyze(Values: list[int]) -> None:
    Sum = 0
    if len(Values) == 0:
        print("No values to analyze.")
    else:
        for Value in Values: # loop through Values list
            Sum += Value
        print(f"There are {len(Values)} integers in the list.")
        Parity = "even" if Sum % 2 == 0 else "odd"
        print(f"Sum of the integers is {Sum} and it's {Parity}.")
    
    return None

def main() -> None:
    print("Program starting.")
    Values = []
    askIntegers(Values)
    analyze(Values)

    print("Program ending.")
    return None
if __name__ == "__main__" :
    main()