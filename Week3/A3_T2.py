print("Program starting.")
print("String comparisons")
Word1 = input("Insert first word: ")
Char = input("Insert a character: ")
if Char in Word1:
    print(f"Word \"{Word1}\" contains character \"{Char}\"")
else:
    print('Word "', Word1, ' doesnt contain character "', Char,'"', sep="")
Word2 = input("Insert a second word: ")
if Word1 < Word2:
    print('The first word "', Word1,'" is before the second word "', Word2,'" alphabetically.', sep="")
elif Word1 > Word2:
    print('The second word "', Word2,'" is before the first word "', Word1,'" alphabetically.', sep="")
else:
    print('Both inserted words are the same alphabetically, "', Word1,'"', sep="")
print("Program ending.")
