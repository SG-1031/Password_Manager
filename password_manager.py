import os
import json
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

DATA_FILE = 'passwords.dat'
SALT_FILE = 'salt.bin'
SALT_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 100_000
BLOCK_SIZE = AES.block_size

def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def derive_key(master_password, salt):
    return PBKDF2(master_password, salt, dkLen=KEY_SIZE, count=ITERATIONS)

def encrypt(data, key):
    data = pad(data)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(data)
    return iv + encrypted

def decrypt(encrypted_data, key):
    iv = encrypted_data[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_data[BLOCK_SIZE:])
    return unpad(decrypted)

def load_data(key):
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'rb') as f:
        encrypted = f.read()
    try:
        decrypted = decrypt(encrypted, key)
        return json.loads(decrypted.decode('utf-8'))
    except Exception:
        print("Incorrect master password or corrupted data.")
        exit()

def save_data(data, key):
    raw = json.dumps(data).encode('utf-8')
    encrypted = encrypt(raw, key)
    with open(DATA_FILE, 'wb') as f:
        f.write(encrypted)

def get_salt():
    if not os.path.exists(SALT_FILE):
        salt = get_random_bytes(SALT_SIZE)
        with open(SALT_FILE, 'wb') as f:
            f.write(salt)
        return salt
    with open(SALT_FILE, 'rb') as f:
        return f.read()

def add_password(data):
    site = input("Enter site/app name: ").strip()
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ").strip()
    data[site] = {'username': username, 'password': password}
    print(f"Password for {site} saved.")

def retrieve_password(data):
    site = input("Enter site/app name to retrieve: ").strip()
    entry = data.get(site)
    if entry:
        print(f"Site: {site}")
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")
    else:
        print("No entry found.")

def delete_password(data):
    site = input("Enter site/app name to delete: ").strip()
    if site in data:
        del data[site]
        print(f"Deleted password entry for {site}.")
    else:
        print("No entry found.")

def main():
    print("=== Password Manager ===")
    master_password = getpass("Enter master password: ")
    salt = get_salt()
    key = derive_key(master_password.encode('utf-8'), salt)

    data = load_data(key)

    while True:
        print("\nOptions: add, retrieve, delete, exit")
        choice = input("Choose an option: ").strip().lower()
        if choice == 'add':
            add_password(data)
            save_data(data, key)
        elif choice == 'retrieve':
            retrieve_password(data)
        elif choice == 'delete':
            delete_password(data)
            save_data(data, key)
        elif choice == 'exit':
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
