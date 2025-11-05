def writeFile(Filename: str, Content: str):
    try:
        with open(Filename, 'w', encoding='UTF-8') as file:
            file.write(Content)
        print("Ciphered text saved!")
    except Exception as e:
        print(f"Error saving file: {e}")

def askRows() -> str:
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)
    return "\n".join(lines)

def shiftCharacter(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    else:
        return char

def rot13(Content: str) -> str:
    result = ""
    for char in Content:
        if char.islower():
            result += shiftCharacter(char, "abcdefghijklmnopqrstuvwxyz")
        elif char.isupper():
            result += shiftCharacter(char, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            result += char
    return result

def main():
    print("Program starting.\n")

    LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
    plain_text = askRows()
    ciphered_text = rot13(plain_text)
    
    print("\n#### Ciphered text ####")
    print(ciphered_text)
    print("\n#### Ciphered text ####")
    
    filename = input("Insert filename to save: ")
    if filename.strip():
        writeFile(filename.strip(), ciphered_text)
    else:
        print("File name not defined.\nAborting save operation.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
