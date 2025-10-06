
# 🔐✨ Simple Password Manager ✨🔐
# ---------------------------------
# This beginner-friendly password manager lets you securely store and view passwords using encryption.
# All passwords are encrypted with a key generated on first run. Keep your 'key.key' file safe!
#
# Features:
#   - Add new passwords
#   - View stored passwords
#   - All data is encrypted for safety
#
# Made for learning and fun! 🐍

from cryptography.fernet import Fernet
import os

# 🗝️ Generate and save a key (only if not already present)
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

if not os.path.exists('key.key'):
    write_key()

# 🗝️ Load the encryption key
def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

# 👀 View all stored passwords
def view():
    print('\n🔎 Saved Passwords:')
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("::")
                try:
                    decrypted = fer.decrypt(passw.encode()).decode()
                    print(f'👤 Account: {user}  |  🔑 Password: {decrypted}')
                except Exception:
                    print(f'👤 Account: {user}  |  🔒 <decryption error>')
    except FileNotFoundError:
        print('⚠️ No passwords saved yet!')

# ➕ Add a new password
def add():
    name = input('👤 Enter Account Name: ')
    pwd = input('🔑 Enter Password: ')
    encrypted = fer.encrypt(pwd.encode()).decode()  # Store as string
    with open('passwords.txt', 'a') as f:
        f.write(name + '::' + encrypted + '\n')
    print('✅ Password added and encrypted!')

# 🚦 Main menu loop
print('\n🔐 Welcome to the Simple Password Manager! 🔐')
print('---------------------------------------------')
while True:
    mode = input('Would you like to ➕ add a new password, 👀 view existing ones, or ❌ quit? (view/add/q): ').strip().lower()
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == 'q':
        print('👋 Goodbye! Stay safe!')
        break
    else:
        print('❌ Invalid mode. Please type "view", "add", or "q".')
