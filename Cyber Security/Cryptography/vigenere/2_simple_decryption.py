def vigenere_decrypt(encrypted_message, key):
    result = ""
    key = key.upper()  # Ensure the key is uppercase
    key_index = 0
    
    for char in encrypted_message:
        if char.isalpha():  # Only process letters
            shift = ord(key[key_index % len(key)]) - ord('A')  # Get shift value from key
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            key_index += 1
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

# Example usage
encrypted_message = "QHE cgfysj"
key = "KEY"
decrypted = vigenere_decrypt(encrypted_message, key)
print(f"Decrypted: {decrypted}")
