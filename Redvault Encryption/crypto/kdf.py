# crypto/kdf.py
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256

def derive_key(password: str, salt: bytes, key_len=32) -> bytes:
    return PBKDF2(
        password.encode(),
        salt,
        dkLen=key_len,
        count=200_000,
        hmac_hash_module=SHA256
    )
