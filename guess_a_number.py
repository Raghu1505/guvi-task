import random
r = random.randrange(1, 100)
print("Guess the number within 10 ATTEMPTS")
guess = int(input("Please enter your guess (1-10): "))
for i in range(9):
        if guess < r:
                print("Your guess is too low")
                guess = int(input("Please enter your guess: "))
        elif guess>r:
                print("Your guess is too high")
                guess = int(input("Please enter your guess: "))
        else:
                print("You win!!!")
                break
print("Game over")
