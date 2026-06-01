import hashlib
import hmac
import os

key = os.urandom(32)
message = b"Transfer 1000 UAH to user5"

mac = hmac.new(key, message, hashlib.sha256).hexdigest()

tampered_message = b"Transfer 9000 UAH to user5"
tampered_mac = hmac.new(key, tampered_message, hashlib.sha256).hexdigest()

print("key =", key.hex())
print("message =", message.decode())
print("mac =", mac)
print("tampered_message =", tampered_message.decode())
print("tampered_mac =", tampered_mac)
print("compare_digest =", hmac.compare_digest(mac, tampered_mac))
