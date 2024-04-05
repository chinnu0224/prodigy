def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.
    
    Parameters:
    text (str): The message to be encrypted or decrypted.
    shift (int): The number of positions to shift the letters.
    encrypt (bool): True for encryption, False for decryption.
    
    Returns:
    str: The encrypted or decrypted message.
    """
    result = ''
    
    # Adjust shift for decryption
    if not encrypt:
        shift = -shift

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            result += char
    
    return result


# User input
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt the message: ").lower()

# Perform encryption or decryption
if operation == 'encrypt':
    encrypted_message = caesar_cipher(message, shift_value, encrypt=True)
    print("Encrypted message:", encrypted_message)
elif operation == 'decrypt':
    decrypted_message = caesar_cipher(message, shift_value, encrypt=False)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid operation. Please type 'encrypt' or 'decrypt'.")
