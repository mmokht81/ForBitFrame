import random
import string

def make_password(length=8):
    pool = string.ascii_letters + string.digits + "!@#$%"
    while True:
        pww = "".join(random.choice(pool) for _ in range(length))
        if any(c.isdigit() for c in pww) and any(c.isupper() for c in pww):
            return pww

while True:
    print("Password is ready: ", make_password())
    Entery = input("Enter no if you dont like the password OR yes for exit: ")
    if Entery == "yes":
        break
    elif Entery == "no":
        continue
    else:
        print("Invalid Entry! ")