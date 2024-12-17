"""
The Caesar cipher can be brute-forced by trying all possible keys (shifts).
This script decrypts an encrypted message by attempting all shifts (1-25) 
and displaying the result for each key.

Formula used for decryption:
    since the encryption is :
        y = (x+k) % 26
    therfor :
        x = (x-k) % 26

Where:
    - x is the original character (decrypted character, wrapped within A-Z)
    - y is the encrypted character (converted to 0-25 range)
    - k is the key (the number of positions to shift back)

Example: Let's brute-force decrypt the message "JGJVFKRRO" which is GDGSCHOOL shifted by k=3.
"""

# Encrypted message to decrypt
encrypted_message = "JGJVFKRRO"

# Function to shift one character backward
def shift_one_character(c, k):
    """
    Shifts a single character backward by the key value k, wrapping around the alphabet.
    Input:
        c: ASCII value of the character (integer)
        k: The shift key
    Output:
        Decrypted character's ASCII value
    """
    return ((c - ord('A') - k) % 26) + ord('A')

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
            original_ascii = ord(m)  # Get the ASCII value of the character
            shifted_ascii = shift_one_character(original_ascii, k)  # Shift the character backward
            decrypted_char = chr(shifted_ascii)  # Convert back to a character
            result += decrypted_char  # Append to the result
        
        print(f"Key = {k}: {result}")

# Main function
def main():
    brute_force_caesar_cipher(encrypted_message)

# Entry point of the script
if __name__ == "__main__":
    main()
