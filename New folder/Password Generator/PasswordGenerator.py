import random
import string

def generate_random_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = []
    
    if length >= 1:
        password.append(random.choice(lowercase))
    if length >= 2:
        password.append(random.choice(uppercase))
    if length >= 3:
        password.append(random.choice(digits))
    if length >= 4:
        password.append(random.choice(special_characters))

    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - len(password))

    
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    password = generate_random_password(length)
    print(f"Generated password: {password}")