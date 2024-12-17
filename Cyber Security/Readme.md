# Cybersecurity
This subfolder contains various cybersecurity-related scripts, including cryptographic algorithms and techniques. 
The primary focus is on demonstrating and implementing classic encryption methods like Caesar Cipher and Vigenere Cipher.

# Project Structure
```
Cyber Security/ 
├── Cryptography/ 
│   ├── Cesar/ 
│   │   ├── 1_cipher.py               # Caesar cipher encryption 
│   │   ├── 2_break_the_cipher.py      # Breaking Caesar cipher 
│   │   ├── 3_cipher_with_upper_lower_chars.py  # Caesar cipher with both upper and lower case 
│   │   └── 4_break_the_cipher.py      # Caesar cipher brute force handle all cases 
│   └── vigenere/ 
│       ├── 1_simple_encryption.py     # Vigenere cipher simple encryption 
│       ├── 2_simple_decryption.py     # Vigenere cipher simple decryption 
│       ├── 3_encryption.py           # Vigenere cipher encryption with case_sensitive_key 
│       ├── 4_decryption.py           # Vigenere cipher decryption with case_sensitive_key 
│       └── 5_break_vigenere.py       # Breaking Vigenere cipher (brute force) 
├── Readme.md                         # Project overview and instructions 
```

# How to Use

### 1. Navigate to the Cryptography folder:

``` 
    cd Cryptography/Cesar 
OR
    cd Cryptography/vigenere 
```
### 2. Choose the desired cipher (Caesar or Vigenère) and run the respective Python script.
` python3 file_name `
## Example
` python3 1_cipher.py `

# Requirements
- Python 3.x
- No additional libraries are required for basic functionality.