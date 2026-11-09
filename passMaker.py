import random
import string
from collections import Counter
random.seed(7)
def make_password(length=12):
    pool = string.ascii_letters + string.digits + "!@#$%"
    while True:
        pw = "".join(random.choice(pool) for _ in range(length))
        if any(c.isdigit() for c in pw) and any(c.isupper() for c in pw):
            return pw
print("رمز پیشنهادی:", make_password())
rolls = [random.randint(1, 6) for _ in range(600)]
counts = Counter(rolls)
for face in range(1, 7):
    print(face, "█" * (counts[face] // 10), counts[face])
    