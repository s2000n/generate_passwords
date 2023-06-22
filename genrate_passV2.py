import random
number_of_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Enter the length of the password: "))
count=0
for j in range(number_of_passwords):
    count=count + 1
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%"
    password = ""
    for i in range(password_length):
      password += random.choice(characters)
    with open("passwords.txt", "a") as file:
      file.write(password + "\n")
    print(count)
