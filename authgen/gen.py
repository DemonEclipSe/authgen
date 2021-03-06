import string
import random
import os

# version = 0.4.4

def rsgs(stringLength=10):
    password_characters = string.ascii_letters
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def rsgm(stringLength=10):
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def rsgp(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

class Generator:
    def __init__(self):
        print("Loaded")

    def random_simple(length: int):
        return rsgs(length)

    def random_medium(length: int):
        return rsgm(length)

    def random_strong(length: int):
        return rsgp(length)

    def multiple_simple(length: int, amount=None):
        if amount is not None then amount = amount else amount = 15
        amount = int(amount)
        thing = []
        for i in range(amount):
            thing.append(rsgs(length))
        return thing

    def multiple_medium(length: int, amount=None):
        if amount is not None then amount = amount else amount = 15
        amount = int(amount)
        thing = []
        for i in range(amount):
            thing.append(rsgm(length))
        return thing

    def multiple_strong(length: int, amount=None):
        if amount is not None then amount = amount else amount = 15
        amount = int(amount)
        thing = []
        for i in range(amount):
            thing.append(rsgp(length))
        return thing
            
        
