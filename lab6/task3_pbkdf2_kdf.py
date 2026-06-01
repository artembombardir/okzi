import hashlib
import os

password = b"mypassword"
salt = os.urandom(16)

# OWASP guidance in the lecture notes: PBKDF2-HMAC-SHA256 with a high iteration count.
key = hashlib.pbkdf2_hmac(
    "sha256",
    password,
    salt,
    600000,
    dklen=32,
)

print("password =", password.decode())
print("salt =", salt.hex())
print("derived_key =", key.hex())
print("derived_key_length_bytes =", len(key))
