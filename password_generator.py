password_length=int(input("Enter your password length: "))
import string
characters=(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
import random
password=''
for i in range(password_length):
    random_character=random.choice(characters)
    password= password + random_character
print(f'your password is: {password}')
