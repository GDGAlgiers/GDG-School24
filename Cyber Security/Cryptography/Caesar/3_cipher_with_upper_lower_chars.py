"""
This implementation works for messages containing both uppercase and lowercase letters.
Non-alphabetic characters remain unchanged.
"""

# The message to encrypt and the encryption key
message = "GdG School!"  # Mixed case message
k = 3  # Key for shifting characters

# Function to shift one character
def shift_one_character(c):
    """
    Shifts a single character by the value of k, wrapping around the alphabet.
    Input:
        c: Character to shift (string, single character)
        k: The shift key (integer)
    Output:
        Encrypted character (string, single character)
    """
    if c.isupper():  # Uppercase letters (A-Z)
        return chr(((ord(c) - ord('A') + k) % 26) + ord('A'))
    elif c.islower():  # Lowercase letters (a-z)
        return chr(((ord(c) - ord('a') + k) % 26) + ord('a'))
    else:
        return c  # Non-alphabetic characters remain unchanged

# Main function to encrypt the message
def main():
    result = ""  # Initialize the result as an empty string
    for m in message:
        encrypted_char = shift_one_character(m)  # Encrypt each character
        result += encrypted_char  # Append to the result
    
    print(f"Encrypted message: {result}")

# Entry point of the script
if __name__ == "__main__":
    main()
