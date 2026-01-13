def encrypt(shift1, shift2):
    text = open("raw_text.txt", "r").read()
    result = ""

    for ch in text:
        # lowercase letters
        if 'a' <= ch <= 'z':
            if ch <= 'm':
                new = ord(ch) + (shift1 * shift2)
            else:
                new = ord(ch) - (shift1 + shift2)

            result += chr((new - 97) % 26 + 97)

        # uppercase letters check
        elif 'A' <= ch <= 'Z':
            if ch <= 'M':
                new = ord(ch) - shift1
            else:
                new = ord(ch) + (shift2 ** 2)

            result += chr((new - 65) % 26 + 65)

        # other characters check
        else:
            result += ch

    open("encrypted_text.txt", "w").write(result)


def decrypt(shift1, shift2):
    text = open("encrypted_text.txt", "r").read()
    result = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            if ch <= 'm':
                new = ord(ch) - (shift1 * shift2)
            else:
                new = ord(ch) + (shift1 + shift2)

            result += chr((new - 97) % 26 + 97)

        elif 'A' <= ch <= 'Z':
            if ch <= 'M':
                new = ord(ch) + shift1
            else:
                new = ord(ch) - (shift2 ** 2)

            result += chr((new - 65) % 26 + 65)

        else:
            result += ch

    open("decrypted_text.txt", "w").write(result)


def verify():
    original = open("raw_text.txt").read()
    decrypted = open("decrypted_text.txt").read()

    if original == decrypted:
        print("Decryption successful")
    else:
        print("Decryption failed")


# Main program

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypt(shift1, shift2)
decrypt(shift1, shift2)
verify()
