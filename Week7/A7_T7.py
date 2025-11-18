ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_config(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines[:3], lines[3]

def rotate(rotor_positions):
    rotor_positions[2] = (rotor_positions[2] + 1) % 26
    if rotor_positions[2] == 0:
        rotor_positions[1] = (rotor_positions[1] + 1) % 26
        if rotor_positions[1] == 0:
            rotor_positions[0] = (rotor_positions[0] + 1) % 26

def forward_pass(c, rotors, positions):
    for i in range(3):
        idx = (ALPHABET.index(c) + positions[i]) % 26
        c = rotors[i][idx]
        c = ALPHABET[(ALPHABET.index(c) - positions[i]) % 26]
    return c

def reverse_pass(c, rotors, positions):
    for i in reversed(range(3)):
        idx = (ALPHABET.index(c) + positions[i]) % 26
        idx = rotors[i].index(ALPHABET[idx])
        c = ALPHABET[(idx - positions[i]) % 26]
    return c

def reflect(c, reflector):
    return reflector[ALPHABET.index(c)]

def enigma_encrypt(text, rotors, reflector):
    rotor_positions = [0, 0, 0]
    result = ""
    for char in text:
        if char not in ALPHABET:
            continue
        rotate(rotor_positions)
        c = forward_pass(char, rotors, rotor_positions)
        c = reflect(c, reflector)
        c = reverse_pass(c, rotors, rotor_positions)
        print(f'Character "{char}" illuminated as "{c}"')
        result += c
    return result

def main():
    config_file = input("Insert config(filename): ").strip()
    plug = input("Insert plugs (y/n)?: ").strip().lower()
    if plug == 'y':
        print("Plugboard not implemented.")
    else:
        print("No extra plugs inserted.")
    rotors, reflector = load_config(config_file)
    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ").upper()
        if not row:
            print("Enigma closing.")
            break
        print()
        result = enigma_encrypt(row, rotors, reflector)
        print(f'Converted row - "{result}".\n')

if __name__ == "__main__":
    main()
