import random
import string

def generate_password(length):
    special_characters = string.punctuation
    alphanumeric_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(alphanumeric_characters + special_characters) for i in range(length - 2))
    password += random.choice(special_characters)
    password += random.choice(special_characters)
    password = ''.join(random.sample(password, len(password)))  # shuffle the password
    return password

# Generate a random password of length 12 with at least 2 special characters
random_password = generate_password(12)
print(random_password)