"""
Vigenère Cipher: Encrypt a message using a case-sensitive repeating keyword.
The key adapts its case to match the message's case.
"""

# Message and keyword
message = "GdG SchoOl"
keyword = "KEY"  # The original key

# Function to shift one character
def shift_character(c, k):
    """
    Shifts a character forward based on the case-sensitive keyword.
    """
    if c.isupper():
        return chr(((ord(c) - ord('A') + k) % 26) + ord('A'))
    elif c.islower():
        return chr(((ord(c) - ord('a') + k) % 26) + ord('a'))
    else:
        return c  # Non-alphabetic character

# Function to generate a case-sensitive repeated key
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

# Function to encrypt the message
def encrypt_vigenere(message, keyword):
    """
    Encrypts a message using the Vigenère cipher.
    """
    result = ""
    case_sensitive_key = generate_case_sensitive_key(message, keyword)
    
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ord(case_sensitive_key[i].upper()) - ord('A')  # Shift based on the key character
            result += shift_character(char, shift)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# Main function
def main():
    encrypted_message = encrypt_vigenere(message, keyword)
    print(f"Message: {message}")
    print(f"Keyword: {keyword}")
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
