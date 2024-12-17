"""
The Caesar cipher is one of the simplest encryption techniques. 
It works by shifting characters in a string using the mathematical formula:

    y = (x + k) % 26

Where:
    - y is the new character (the encrypted character, wrapped within A-Z)
    - x is the old character (the original character, converted to 0-25 range)
    - k is the key (the number of positions to shift)

For example, let's encrypt the string "GDGSCHOOL" with a key of k = 3.
"""

# The message to encrypt and the encryption key
message = "GDGSCHOOL"
k = 3  # Key for shifting characters

# Function to shift one character
def shift_one_character(c):
    """
    Shifts a single character by the value of k, wrapping around the alphabet.
    Input:
        c: ASCII value of the character (integer)
    Output:
        Encrypted character's ASCII value
    """
    # Convert ASCII to 0-25 range (A=0, B=1, ..., Z=25), apply shift and modulo, then convert back to ASCII
    # We gonna use c - ord('A') because ord('A') == 65 since we want to count from 0 not from 65

    return ((c - ord('A') + k) % 26) + ord('A')

# Main function to encrypt the message
def main():
    result = ""  # Initialize the result as an empty string
    for m in message:
        original_ascii = ord(m)  # Get the ASCII value of the character
        shifted_ascii = shift_one_character(original_ascii)  # Shift the character within A-Z
        encrypted_char = chr(shifted_ascii)  # Convert back to a character
        result += encrypted_char  # Append to the result
    
    print(f"Encrypted message: {result}")

# Entry point of the script
if __name__ == "__main__":
    main()



'''
    remarque: 
        this code will only work with uppercase letters 
        to make it work with lowercase letters, change ord('A') to ord('a')
        and the message should be lowercase also 
        ex: message = "gdgschool"
'''