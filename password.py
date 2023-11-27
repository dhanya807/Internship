import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password():
    print("Password Generator\n")

    try:
        length = int(input("Enter the desired password length: "))
        no = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    if length <= 0 or no <= 0:
        print("Please enter positive values for length and count.")
        return

    print("\nGenerated Passwords:")
    for i in range(no):
        password = generate_password(length)
        print(password)


password()