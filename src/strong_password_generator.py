import random
import string

def generate_password():
    length = random.randint(12, 20)
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(random.choice(chars) for _ in range(length))


with open("data/strong_passwords.txt", "w", encoding="utf-8") as f:
    for _ in range(9484088):
        f.write(generate_password() + "\n")