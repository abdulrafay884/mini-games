import random
import string
pass_len = int(input("Enter The Length Of The Password:"))
val = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password +=random.choice(val)
print(f"Your Password Is: {password}")