DELIMITER = ','

def collectWords():
    words = []
    word = input("Insert word(empty stops): ")
    while word != "":
        words.append(word)
        word = input("Insert word(empty stops): ")
    return DELIMITER.join(words)

def analyseWords(data):
    words = data.split(DELIMITER)
    total_chars = sum(len(w) for w in words)
    print(f"- {len(words)} Words")
    print(f"- {total_chars} Characters")
    print("- {:.2f} Average word length".format(total_chars / len(words)))

def main():
    print("Program starting.")
    collected = collectWords()
    analyseWords(collected)
    print("Program ending.")

if __name__ == "__main__":
    main()
