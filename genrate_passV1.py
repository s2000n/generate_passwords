import random

def generate_password(x):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%"
  global password_length
  password_length = x
  password = ""
  for i in range(password_length):
    password += random.choice(characters)
  return password

def save_password(password):
  with open("passwords.txt", "a") as file:
    file.write(password + "\n")

def select_number_of_passwords():
  number_of_passwords = int(input("How many passwords do you want to generate? "))
  return number_of_passwords

if __name__ == "__main__":
  number_of_passwords = select_number_of_passwords()
  password_length = int(input("Enter the length of the password: "))
  for _ in range(number_of_passwords):
    password = generate_password(password_length)
    save_password(password)
