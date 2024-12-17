def vigenere_encrypt(message, key):
    result = ""
    key = key.upper()  # Ensure the key is uppercase
    key_index = 0
    
    for char in message:
        if char.isalpha():  # Only process letters
            shift = ord(key[key_index % len(key)]) - ord('A')  # Get shift value from key
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

# Example usage
message = "GDG school"
key = "KEY"
encrypted = vigenere_encrypt(message, key)
print(f"Encrypted: {encrypted}")
