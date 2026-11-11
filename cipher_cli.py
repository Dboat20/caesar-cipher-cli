#!/usr/bin/env python3
"""
Caesar Cipher CLI
-----------------
Encryption algorithm used: CAESAR CIPHER (substitution cipher with a numeric shift key).

Usage:
    Interactive menu:   python cipher_cli.py
    One-shot commands:  python cipher_cli.py encrypt "Hello, World!" --shift 3
                        python cipher_cli.py decrypt "Khoor, Zruog!" --shift 3
"""

import argparse
import sys

ALGORITHM = "Caesar Cipher"


def shift_text(text: str, shift: int) -> str:
    """Shift every letter by `shift` positions; keep case, leave other characters unchanged."""
    result = []
    for ch in text:
        if "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        else:
            result.append(ch)
    return "".join(result)


def encrypt(plain_text: str, shift: int) -> str:
    return shift_text(plain_text, shift)


def decrypt(cipher_text: str, shift: int) -> str:
    return shift_text(cipher_text, -shift)


def ask_shift() -> int:
    while True:
        raw = input("Enter shift key (integer, e.g. 3): ").strip()
        try:
            return int(raw)
        except ValueError:
            print("  Invalid key. Please enter a whole number.")


def interactive() -> None:
    print("=" * 44)
    print(f" Text Encryption Tool  |  Algorithm: {ALGORITHM}")
    print("=" * 44)
    while True:
        print("\n1) Encrypt text")
        print("2) Decrypt text")
        print("3) Quit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            text = input("Enter plain text: ")
            shift = ask_shift()
            print(f"Encrypted text: {encrypt(text, shift)}")
        elif choice == "2":
            text = input("Enter cipher text: ")
            shift = ask_shift()
            print(f"Decrypted text: {decrypt(text, shift)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


def main() -> None:
    parser = argparse.ArgumentParser(description=f"Encrypt/decrypt text using the {ALGORITHM}.")
    sub = parser.add_subparsers(dest="command")
    for name in ("encrypt", "decrypt"):
        p = sub.add_parser(name, help=f"{name} a piece of text")
        p.add_argument("text", help="the text to process (use quotes)")
        p.add_argument("--shift", "-s", type=int, required=True, help="integer shift key")

    args = parser.parse_args()
    if args.command == "encrypt":
        print(encrypt(args.text, args.shift))
    elif args.command == "decrypt":
        print(decrypt(args.text, args.shift))
    else:
        try:
            interactive()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
