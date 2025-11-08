LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
   
    if isinstance(shift, str):
        alphabet = shift
        half = len(alphabet) // 2
        
        if char in alphabet:
            idx = alphabet.index(char)
            return alphabet[(idx + half) % len(alphabet)]
        
        lower_alphabet = alphabet.lower()
        if char.lower() in lower_alphabet:
            idx = lower_alphabet.index(char.lower())
            res = lower_alphabet[(idx + half) % len(lower_alphabet)]
            return res.upper() if char.isupper() else res
        return char

  
    try:
        shift_amount = int(shift)
    except (TypeError, ValueError):
        
        return char

    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift_amount) % 26 + base)
    else:
        return char

def rot13(Content: str) -> str:
    result = ""
    for char in Content:
        if char.isalpha():
            result += shiftCharacter(char, 13)
        else:
            result += char
    return result

def main():
    print("Program starting.\n")

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

