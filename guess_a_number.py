import random
r = random.randrange(1, 10)
guess = int(input("Please enter your guess (1-10): "))
while( guess!=r):
        if guess < r:
                print("Your guess is too low")
                guess = int(input("Please enter your guess: "))
        elif guess>r:
                print("Your guess is too high")
                guess = int(input("Please enter your guess: "))
print("Hit")
