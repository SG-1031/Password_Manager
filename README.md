# Password Manager

## Overview

A simple command-line password manager that stores passwords encrypted with a master password using AES encryption.

## Features

- Add, retrieve, and delete password entries
- Data encrypted with master password
- Uses Password-Based Key Derivation Function 2 (PBKDF2) for key derivation and AES CBC mode for encryption
- Stores data locally in encrypted form

## Install the `pycryptodome` library

-  This script uses the Crypto package from PyCryptodome for encryption and key derivation. You can install it using pip:

    ```bash
    pip install pycryptodome

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
- Troubleshooting: "Defaulting to user installation because normal site-packages is not writeable"

    The message: "Defaulting to user installation because normal site-packages is not writeable." means that `pip` doesn't have permission to install packages system-wide (usually because you’re not running it as an administrator or with root privileges). Instead, it installs the packages just for your user account.
    
    ---
    
    Is this a problem?
    
    No, this is normal and usually safe. It means:
    
    - Packages are installed in your user directory, not globally.
    - You can still use the packages normally when running Python as your user.
    
    ---
    
    What to do if you want to avoid this message?
    
    1. Run with elevated privileges (if you have permission):
    
    - On Linux/macOS:
    
    ```bash
    sudo pip install -r requirements.txt
    ```
    - On Windows, run Command Prompt as Administrator, then run:
    
    ```cmd
    pip install -r requirements.txt
    ```
    
    2. Use a virtual environment (recommended for Python projects):
    
    - Create a virtual environment:
    
    ```bash
    python -m venv venv
    ```
    
    3. Activate it:
    
    - On Windows:
    
    ```cmd
    venv\Scripts\activate
    ```
    - On macOS/Linux:
    
    ```bash
    source venv/bin/activate
    ```
    
    4. Install packages inside the virtual environment:
    
    ```bash
    pip install -r requirements.txt
    ```
    
    Using a virtual environment keeps dependencies isolated and avoids permission issues.
    

---

## License

This project is for educational purposes only.

---

© 2025 Subash Gurung
