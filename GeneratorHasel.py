import random
import string

length = int(input("Z ilu znaków ma się składać hasło? "))

characters = list(string.ascii_letters + string.digits + string.punctuation)
random.shuffle(characters)

password = []

for x in range(length):
    password.append(random.choice(characters))

print("".join(password))



