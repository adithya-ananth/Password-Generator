import random

password = ""

l = [chr(x) for x in range (ord('a'), ord('z') + 1)]
l.extend([chr(x) for x in range (ord('A'), ord('Z') + 1)])
l.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

length = int(input("\nEnter the length of the password you want: "))

for i in range(0, length):
    password += ''.join(random.choice(l))

print("\nYour new password is:", password)
