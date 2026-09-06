import string
import random
password_length=int(input("Enter your password length: "))
characters=(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
password=''
for i in range(password_length):
    random_character=random.choice(characters)
    password= password + random_character
print(f'your password is: {password}')
