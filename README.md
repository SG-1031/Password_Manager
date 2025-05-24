# Password Manager

## Overview

A simple command-line password manager that stores passwords encrypted with a master password using AES encryption.

## Features

- Add, retrieve, and delete password entries
- Data encrypted with master password
- Uses Password-Based Key Derivation Function 2 (PBKDF2) for key derivation and AES CBC mode for encryption
- Stores data locally in encrypted form

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Run the password manager:


   ```bash
   python password_manager.py

## Usage

- Enter your master password (create one on first run)
- Use options `add`, `retrieve`, `delete`, or `exit`
- Passwords are saved encrypted locally in `passwords.dat`

## Security Notes

- Keep your master password secure and do not forget it; data cannot be recovered without it.
- This is a simple demo, not for production use.

---

## Troubleshooting

- If you enter an incorrect master password, the program will notify you and exit.  
- To start fresh, you can delete `passwords.dat` and `salt.bin`, but you will lose all saved data.

---

## License

This project is for educational purposes only.

---

© 2025 Subash Gurung
