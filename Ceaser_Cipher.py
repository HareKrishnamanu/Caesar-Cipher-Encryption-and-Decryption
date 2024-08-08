def encrypt(text, shift):
    result = ""

    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetical characters remain the same
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25): "))

    if choice == 'E':
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")
    elif choice == 'D':
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
