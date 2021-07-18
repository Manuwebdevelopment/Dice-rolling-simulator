import random
import time
guess_taken = int(input("Whats your guess?\n"))
computer_dice = random.randint(1,6)
print("The computer is rolling the dice....")
time.sleep(3)
print(computer_dice)

if computer_dice == guess_taken:
    print("Good job! You guessed the exact number!") 
else:
    print("Nope. Try again!")

