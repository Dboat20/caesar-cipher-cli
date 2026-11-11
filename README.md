# Caesar Cipher CLI

**Index Number:** 10353232
**Name:** Dennis Boateng

A command-line program that encrypts and decrypts text in the terminal.

## Encryption Algorithm Used

**Caesar Cipher**: a substitution cipher where each letter is shifted by a fixed number of positions (the key) in the alphabet.

- Encryption: `E(x) = (x + key) mod 26`
- Decryption: `D(x) = (x - key) mod 26`
- Upper/lower case is preserved; digits, spaces and punctuation are left unchanged.

Example: `Hello, World!` with key `3` → `Khoor, Zruog!`

## Requirements

- Python 3.6+ (no external libraries)

## How to Run

### Interactive mode
```bash
python cipher_cli.py
```
Choose 1 to encrypt, 2 to decrypt, 3 to quit. Enter your text and a numeric shift key when prompted.

### One-shot mode
```bash
python cipher_cli.py encrypt "Hello, World!" --shift 3
python cipher_cli.py decrypt "Khoor, Zruog!" --shift 3
```

## Sample Session
```
1) Encrypt text
2) Decrypt text
3) Quit
Choose an option (1-3): 1
Enter plain text: Hello, World!
Enter shift key (integer, e.g. 3): 3
Encrypted text: Khoor, Zruog!
```

## Note
The Caesar Cipher is for learning purposes only and is not secure for real-world use.
