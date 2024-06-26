import random
import RandomCarrot as carrot

# Lines of code to display random numbers
def random_number_generator():
    number = random.randint(1, 1000)
    print(number)

def randomnumber():
    carrot.random_number_generator()

# Lines of code to display random letters
def random_letters_generator(length=1):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

def randomletters():
    carrot.random_letters_generator()

# Lines of code to make both random numbers and letters

def both_numbers_letters_generator(length=1):
    numbers = random.randint(1, 1000) 
    letters = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
    return {'numbers': numbers, 'letters': letters}

def both(length=1):
    result = both_numbers_letters_generator(length)
    print(result["numbers"])
    print(result["letters"])
