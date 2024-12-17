"""
Brute-force the Vigenère Cipher with a case-sensitive repeating key.
"""

import itertools
import string

# Encrypted message to brute force
encrypted_message = "QhE CgfySj"    # encrypted "GdG SchoOl"
possible_characters = string.ascii_uppercase  # Possible key characters
key_length = 3  # Assume key length is known (can be adjusted) btw key="KEY"


def shift_character_back(c, k):
    """
    Shifts a character backward based on the case-sensitive keyword.
    """
    if c.isupper():
        return chr(((ord(c) - ord('A') - k + 26) % 26) + ord('A'))
    elif c.islower():
        return chr(((ord(c) - ord('a') - k + 26) % 26) + ord('a'))
    else:
        return c  # Non-alphabetic character


def generate_case_sensitive_key(message, keyword):
    """
    Repeats the keyword to match the length and case of the message.
    """
    repeated_key = []
    keyword_length = len(keyword)
    j = 0  # Index for the keyword
    for char in message:
        if char.isalpha():  # Only match alphabetic characters
            if char.isupper():
                repeated_key.append(keyword[j % keyword_length].upper())
            elif char.islower():
                repeated_key.append(keyword[j % keyword_length].lower())
            j += 1
        else:
            repeated_key.append(char)  # Non-alphabetic characters are ignored
    return "".join(repeated_key)
# Function to decrypt the message
def decrypt_vigenere(encrypted_message, keyword):
    """
    Decrypts a message using the Vigenère cipher.
    """
    result = ""
    case_sensitive_key = generate_case_sensitive_key(encrypted_message, keyword)
    
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            shift = ord(case_sensitive_key[i].upper()) - ord('A')  # Shift based on the key character
            result += shift_character_back(char, shift)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# Function to brute force Vigenère cipher
def brute_force_vigenere(encrypted_message, key_length):
    """
    Brute-forces the Vigenère cipher by trying all keys of a given length.
    """
    print(f"Brute-forcing with key length = {key_length}...\n")
    for key in itertools.product(possible_characters, repeat=key_length):
        key_str = "".join(key)
        decrypted_message = decrypt_vigenere(encrypted_message, key_str)
        print(f"Key: {key_str} -> Decrypted: {decrypted_message}")

# Main function
def main():
    brute_force_vigenere(encrypted_message, key_length)

if __name__ == "__main__":
    main()
