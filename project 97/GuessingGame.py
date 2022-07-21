import random 

number = random.randint(1,9)
chances = 0
print("Guess a number between 1-9: ")

while chances < 5: 
    Guess = int(input("enter your guess: "))
    if Guess == number:
        print("You Won!")
        break
    elif Guess < number:
        print("Too Low")
    else:
        print("Too High")
    chances += 1

if not chances < 5:
    print("You Lose")