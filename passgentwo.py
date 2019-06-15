import random

# Set a variable with all the characters we want available for this password generator
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

# Get the length user would like the password to be - set as variable length
length = input("How many characters for this password? ")
length = int(length) # Convert input to INT

# Get how many passwords the user would like to choose from - set as prange variable
prange = input('How many passwords would you like to choose from?')
prange = int(prange) # Convert input to INT

# Create amount of passwords requested and in the length requested
for p in range(prange):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)