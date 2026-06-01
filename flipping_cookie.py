import requests

BASE = "https://aes.cryptohack.org/flipping_cookie"

def xor_bytes(a: bytes, b: bytes, c: bytes) -> bytes:
    return bytes(x ^ y ^ z for x, y, z in zip(a, b, c))

def main() -> None:
    cookie = requests.get(f"{BASE}/get_cookie/", timeout=20).json()["cookie"]

    iv = bytes.fromhex(cookie[:32])
    ciphertext = cookie[32:]

    old = b"admin=False"
    new = b"admin=True;"

    iv_new = xor_bytes(iv[:len(new)], old, new) + iv[len(new):]

    r = requests.get(f"{BASE}/check_admin/{ciphertext}/{iv_new.hex()}/", timeout=20)
    r.raise_for_status()
    print(r.json())

if __name__ == "__main__":
    main()