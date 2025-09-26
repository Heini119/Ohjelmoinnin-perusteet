print("Program starting.")
print("Testing decision structures.")
Integer = int(input("Insert an integer: "))
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
ChoiceO = input("Your choice: ")
if (ChoiceO == "1"):
    if Integer >= 400:
        Sum = (Integer + 44)
        print("Using one multi-branched decision structure.")
        print(f"Result is {Sum}")
        print()
        print("Program ending.")
    elif Integer >= 200:
        Sum = (Integer + 22)
        print("Using one multi-branched decision structure.")
        print(f"Result is {Sum}")
        print()
        print("Program ending.")
    elif Integer >= 100:
        Sum = (Integer + 11)
        print("Using one multi-branched decision structure.")
        print(f"Result is {Sum}")
        print()
        print("Program ending.")
    else:
        print("Using one multi-branched decision structure.")
        print(f"Result is {Integer}")
        print()
        print("Program ending.")
elif (ChoiceO == "2"):
    if Integer >= 400:
        Sum = (Integer + 44)
        print("Using multiple independent if-statements structure.")
        print(f"Result is {Sum}")
        print()
        print("Program ending.")
    if Integer >= 200:
        Sum = (Integer + 22)
        print("Using one multi-branched decision structure.")
        print(f"Result is {Sum}")
        print()
        print("Program ending.")
    if Integer >= 100:
        Sum = (Integer + 11)
        print("Using one multi-branched decision structure.")
        print(f"Result is {Sum}")
        print()
        print("Program ending.")
elif (ChoiceO == "0"):
    print("Exiting...")
    print()
    print("Program ending.")
else:
    print("Unknown option.")
    print()
    print("Program ending.")
