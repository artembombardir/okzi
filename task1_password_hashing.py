from argon2 import PasswordHasher

users = {
    "user1": "password123",
    "user2": "qwerty",
    "user3": "hello123",
    "user4": "admin123",
    "user5": "test123",
}

# OWASP recommends a slow password hashing scheme; Argon2id is a suitable choice.
ph = PasswordHasher(time_cost=2, memory_cost=19456, parallelism=1, hash_len=32, salt_len=16)

records = {}
for username, password in users.items():
    records[username] = ph.hash(password)

for username, password_hash in records.items():
    print(f"{username}: {password_hash}")

# Verify without storing plaintext
print("verify(user1, password123) =", ph.verify(records["user1"], "password123"))
