from random import randint
number = randint(1, 100)
guess = 0
while (guess != number):
    guess = int(input("What's my number? (1-100)"))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("You got it!")