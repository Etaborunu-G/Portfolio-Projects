# 🔐 RedVault — Secure Text File Encryption App

RedVault is a desktop encryption application built with **Python**, **PySide6 (Qt)**, and **PyCryptodome**.
It provides **password-based encryption** with a **backup recovery key**, wrapped in a modern dark-themed GUI with red accents.

This project is designed for **educational and portfolio purposes**, demonstrating applied cryptography, secure key derivation, and modular desktop application architecture.

---

## ✨ Features

- 🔒 Password-based encryption using PBKDF2 (HMAC-SHA256)
- 🗝️ Backup Recovery Key (used if password is forgotten)
- 🖥️ Modern desktop GUI (PySide6 / Qt)
- 🌙 Dark theme with red accents
- 🧩 Clean, modular project structure
- ⚠️ Explicit data safety warnings
- 🪟 Can be compiled into a standalone Windows `.exe`

---

## 📁 Project Structure

redvault/
├── main.py
├── style.py
├── utils.py
│
├── crypto/
│   ├── __init__.py
│   ├── engine.py
│   ├── kdf.py
│   └── format.py
│
└── ui/
    ├── __init__.py
    ├── main_window.py
    ├── encrypt_tab.py
    └── decrypt_tab.py

---

## ⚠️ IMPORTANT USAGE NOTICE

THIS APPLICATION ONLY SUPPORTS **TEXT-BASED FILES CONTAINING READABLE WORDS**.

Supported examples:
- .txt
- .md
- .csv
- .log
- plain-text .json

### ❌ Unsupported File Types

Encrypting or decrypting the following may result in **irreversible data loss**:

- Images (.png, .jpg, .jpeg)
- PDFs
- Word documents (.docx)
- Executables or binary files

---

## 🚨 Responsibility Disclaimer

By using this application, you acknowledge that:

- You are responsible for verifying file compatibility
- You have backups of important data
- The application and its developer are **NOT responsible for lost or corrupted data**

---

## ▶️ How to Run (Development)

### 1. Install Python
Ensure Python **3.10+** is installed:

python --version

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run the Application

python main.py

---

## 🔐 Encryption Overview

1. User enters a password
2. A cryptographic key is derived using PBKDF2
3. A random Backup Recovery Key is generated
4. File is encrypted using AES
5. Backup key is displayed once and must be saved

⚠️ Passwords cannot be recovered.  
If the password is lost, the Backup Recovery Key is required.

---

## 🧱 Build as a Windows Executable (.exe)

### Install PyInstaller

pip install pyinstaller

### Build

python -m PyInstaller --noconfirm --onefile --windowed --name RedVault main.py

### Output

dist/RedVault.exe

The executable runs without requiring Python to be installed.

---

## 🛠️ Technologies Used

- Python 3
- PySide6 (Qt)
- PyCryptodome
- PyInstaller

---

## 📌 Educational Disclaimer

This software is intended for learning and portfolio demonstration purposes only.
It is **not** intended to replace enterprise-grade encryption solutions.

---

## 📜 License

Provided as-is, without warranty of any kind.
