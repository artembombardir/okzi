import requests

BASE = "https://aes.cryptohack.org/lazy_cbc"

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def get_ciphertext() -> bytes:
    plain = b"a" * 48
    r = requests.get(f"{BASE}/encrypt/{plain.hex()}/", timeout=20)
    r.raise_for_status()
    return bytes.fromhex(r.json()["ciphertext"])

def get_decrypted_hex(fake_ciphertext: bytes) -> bytes:
    r = requests.get(f"{BASE}/receive/{fake_ciphertext.hex()}/", timeout=20)
    r.raise_for_status()
    data = r.json()
    if "error" not in data:
        raise RuntimeError(f"Unexpected response: {data}")
    return bytes.fromhex(data["error"].split("Invalid plaintext: ")[1])

def main() -> None:
    ct = get_ciphertext()
    c0 = ct[:16]
    fake = c0 + b"\x00" * 16 + c0

    decrypted = get_decrypted_hex(fake)
    key = xor_bytes(decrypted[:16], decrypted[32:48])

    flag_hex = requests.get(f"{BASE}/get_flag/{key.hex()}/", timeout=20).json()["plaintext"]
    flag = bytes.fromhex(flag_hex).decode()

    print("KEY =", key.hex())
    print("FLAG =", flag)

if __name__ == "__main__":
    main()
