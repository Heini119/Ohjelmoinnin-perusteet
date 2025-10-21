def frameWord(pWord):
    frameLength = len(pWord) + 4
    print("*" * frameLength)
    print(f"* {pWord} *" )
    print("*" * frameLength)
    return None

def main():
    print("Program starting.")
    Word = input("Insert word: ")
    print()
    frameWord(Word)
    print()
    print("Program ending.")
    return None

main()


