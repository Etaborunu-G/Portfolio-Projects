# crypto/engine.py
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

from crypto.format import *
from crypto.kdf import derive_key


def encrypt_file(input_path, output_path, password):
    salt = get_random_bytes(SALT_SIZE)
    iv = get_random_bytes(IV_SIZE)

    backup_key = get_random_bytes(BACKUP_KEY_SIZE)
    password_key = derive_key(password, salt)

    with open(input_path, "rb") as f:
        plaintext = f.read()

    cipher = AES.new(password_key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Wrap backup key using password key
    wrap_cipher = AES.new(password_key, AES.MODE_CBC, iv)
    wrapped_backup = wrap_cipher.encrypt(pad(backup_key, AES.block_size))

    with open(output_path, "wb") as f:
        f.write(
            MAGIC +
            bytes([VERSION]) +
            bytes([MODE_PASSWORD]) +
            salt +
            iv +
            wrapped_backup +
            ciphertext
        )

    return backup_key.hex()


def decrypt_with_password(enc_path, output_path, password):
    with open(enc_path, "rb") as f:
        magic = f.read(4)
        if magic != MAGIC:
            raise ValueError("Invalid file format")

        version = f.read(1)
        f.read(1)  # mode

        salt = f.read(SALT_SIZE)
        iv = f.read(IV_SIZE)
        wrapped_backup = f.read(48)
        ciphertext = f.read()

    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_path, "wb") as f:
        f.write(plaintext)


def decrypt_with_backup_key(enc_path, output_path, backup_key_hex):
    backup_key = bytes.fromhex(backup_key_hex)

    with open(enc_path, "rb") as f:
        f.read(4 + 1 + 1)  # magic + version + mode
        f.read(SALT_SIZE)
        iv = f.read(IV_SIZE)
        f.read(48)        # wrapped backup key
        ciphertext = f.read()

    cipher = AES.new(backup_key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_path, "wb") as f:
        f.write(plaintext)
