"""
Brute-forcing the Caesar cipher that works with both uppercase and lowercase letters.
Non-alphabetic characters (spaces, punctuation, ...) remain unchanged.

For decryption:
    y = ((x - k) % 26) + base

Where:
    - x is the ASCII value of the encrypted character.
    - k is the key (number of positions to shift back).
    - base is ord('A') for uppercase letters or ord('a') for lowercase letters.

The script will try all keys from 1 to 25 and display the decrypted result for each key.
"""

# Encrypted message to brute-force
encrypted_message = "JgJ Vfkrro!"  # Example encrypted message

# Function to shift one character backward
def shift_one_character(c, k):
    """
    Shifts a single character backward by the key value k, wrapping around the alphabet.
    Input:
        c: Character to shift (string, single character)
        k: The shift key (integer)
    Output:
        Decrypted character (string, single character)
    """
    if c.isupper():  # Uppercase letters (A-Z)
        return chr(((ord(c) - ord('A') - k) % 26) + ord('A'))
    elif c.islower():  # Lowercase letters (a-z)
        return chr(((ord(c) - ord('a') - k) % 26) + ord('a'))
    else:
        return c  # Non-alphabetic characters remain unchanged

# Function to brute-force the Caesar cipher
def brute_force_caesar_cipher(message):
    """
    Attempts to decrypt the message by trying all possible keys (1-25).
    Input:
        message: The encrypted message (string)
    Output:
        Prints all possible decrypted results with their corresponding key.
    """
    print("Attempting to brute-force the Caesar cipher...\n")
    for k in range(1, 26):  # Try all keys from 1 to 25
        result = ""  # Initialize decrypted result as an empty string
        for m in message:
            decrypted_char = shift_one_character(m, k)  # Shift character backward
            result += decrypted_char  # Append to the result
        
        print(f"Key = {k}: {result}")

# Main function
def main():
    brute_force_caesar_cipher(encrypted_message)

# Entry point of the script
if __name__ == "__main__":
    main()
