password_length=int(input("Enter your password length: "))
import string
charachters=(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
import random
password=''
for i in range(password_length):
    random_charachter=random.choice(charachters)
    password= password + random_charachter
print(f'your password is: {password}')