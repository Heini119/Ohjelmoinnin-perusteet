
print("Program starting.\n")

words = []
while True:
    Word = input("Insert word (empty stops): ")
    if Word == "":
        break
    words.append(Word)

total_words = len(words)
total_characters = sum(len(Word) for Word in words)

print("\nYou inserted:")
print(f"- {total_words} words")
print(f"- {total_characters} characters")

print("\nProgram ending.")

    