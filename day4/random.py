# make a random number generator
# import random module
import random
import secrets

# generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)

print(secrets.randbelow(100))
