# Password Manager

## Overview

A simple command-line password manager that stores passwords encrypted with a master password using AES encryption.

## Features

- Add, retrieve, and delete password entries
- Data encrypted with master password
- Uses PBKDF2 for key derivation and AES CBC mode for encryption
- Stores data locally in encrypted form

## Setup

1. Install dependencies:
   
'pip install -r requirements.txt'

3. Run the password manager:

'python password_manager.py'

## Usage

- Enter your master password (create one on first run)
- Use options `add`, `retrieve`, `delete`, or `exit`
- Passwords are saved encrypted locally in `passwords.dat`

## Security Notes

- Keep your master password secure and do not forget it; data cannot be recovered without it.
- This is a simple demo, not for production use.

---

© 2025 Subash Gurung
