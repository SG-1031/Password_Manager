# Password Manager - User Guide

## Introduction

This is a simple command-line Password Manager that securely stores your passwords encrypted with a master password. It uses AES encryption and PBKDF2 key derivation to protect your data.

---

## Setup Instructions

1. **Install Python 3**  
   Ensure Python 3 is installed on your system.  
   Check by running:
     
   ```bash
   python --version 

If not installed, download it from [python.org](https://www.python.org/downloads/).

2. **Download Project Files**  
Create a project folder and save the following files inside it:  
- `password_manager.py`  
- `requirements.txt`  
- `README.md` (optional)  
- `GUIDE.md` (this guide)

3. **Install Dependencies**  
Open a terminal or command prompt, navigate to the project folder, and run:  

---

## Running the Password Manager

Run the program by typing:  

---

## How to Use

- **Master Password:**  
  On first run, enter a master password of your choice. This will encrypt your saved passwords.  
  **Important:** Remember this password! If lost, your data cannot be recovered.

- **Menu Options:**  
  After entering the master password, you will see options:  
  - `add` — Add a new password entry  
  - `retrieve` — Retrieve an existing password entry  
  - `delete` — Delete a password entry  
  - `exit` — Exit the program

- **Adding an Entry:**  
  Enter the site/app name, username, and password when prompted.

- **Retrieving an Entry:**  
  Enter the site/app name to view stored credentials.

- **Deleting an Entry:**  
  Enter the site/app name to remove it from storage.

---

## Data Storage

- Password data is encrypted and saved locally in a file named `passwords.dat`.  
- A salt is stored in `salt.bin` for key derivation.

---

## Security Notes

- The master password is critical — do not forget it.  
- This is a learning/demo tool and should not be used for storing sensitive production credentials.  
- Always use strong, unique passwords for your accounts.

---

## Troubleshooting

- If you enter an incorrect master password, the program will notify you and exit.  
- To start fresh, you can delete `passwords.dat` and `salt.bin`, but you will lose all saved data.

---

## License

This project is for educational purposes only.

---

© 2025 Subash Gurung
