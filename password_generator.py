import random

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-?><"
length = int(input("Enter length of password"))
password =''
for i in range(length):
    password += random.choice(string)
    
print(password)