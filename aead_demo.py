from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
import os

def demo_chacha() -> None:
    key = ChaCha20Poly1305.generate_key()
    cipher = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    plaintext = b"Secret message"

    ciphertext = cipher.encrypt(nonce, plaintext, None)
    recovered = cipher.decrypt(nonce, ciphertext, None)
    print("ChaCha20-Poly1305 decrypted =", recovered)

    tampered = bytearray(ciphertext)
    tampered[0] ^= 1

    try:
        cipher.decrypt(nonce, bytes(tampered), None)
    except InvalidTag:
        print("ChaCha20-Poly1305 tampered =", "InvalidTag")

def demo_gcm() -> None:
    key = AESGCM.generate_key(bit_length=128)
    cipher = AESGCM(key)
    nonce = os.urandom(12)
    plaintext = b"Attack at dawn"

    ciphertext = cipher.encrypt(nonce, plaintext, None)
    recovered = cipher.decrypt(nonce, ciphertext, None)
    print("AES-GCM decrypted =", recovered)

    tampered = bytearray(ciphertext)
    tampered[-1] ^= 1

    try:
        cipher.decrypt(nonce, bytes(tampered), None)
    except InvalidTag:
        print("AES-GCM tampered =", "InvalidTag")

if __name__ == "__main__":
    demo_chacha()
    demo_gcm()