def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            if mode == "encrypt":
                new_position = (ord(char) - start + shift) % 26
            else:
                new_position = (ord(char) - start - shift) % 26

            result += chr(start + new_position)

        else:
            result += char

    return result


print("=== Caesar Cipher ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

if mode == "encrypt" or mode == "decrypt":
    encrypted_message = caesar_cipher(message, shift, mode)
    print("Result:", encrypted_message)
else:
    print("Invalid mode. Please choose encrypt or decrypt.")
