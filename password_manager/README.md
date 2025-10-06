# 🔐✨ Simple Password Manager ✨🔐

A beginner-friendly password manager for securely storing and viewing passwords using encryption. All passwords are encrypted with a key generated on first run. Keep your `key.key` file safe!

## Features
- 🗝️ Secure password storage with encryption
- ➕ Add new passwords
- 👀 View stored passwords
- 🐍 Simple and easy to use

## How to Run
```bash
python password_manager.py
```

## How to Use
1. Choose to ➕ add a new password, 👀 view existing ones, or ❌ quit.
2. Passwords are encrypted and stored securely in `passwords.txt`.
3. View your passwords anytime (only with the correct encryption key).

## Example
```
🔐 Welcome to the Simple Password Manager! 🔐
---------------------------------------------
Would you like to ➕ add a new password, 👀 view existing ones, or ❌ quit? (view/add/q): add
👤 Enter Account Name: email
🔑 Enter Password: mySecret123
✅ Password added and encrypted!
```

## Notes
- The encryption key is stored in `key.key`. Do not delete this file, or you will lose access to your passwords.
- Old passwords saved in a different format may show a decryption error.

## License
This project is for educational purposes.

🌟 Made with Python and creativity! 🌟
