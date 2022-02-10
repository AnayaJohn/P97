import random

number= random.randint(1,9)
chances= 0

print ("Number Guessing Game")
print ("Guess a Number between (1-9)")


while chances<5:
    guess= int(input("Enter your number: "))

    if guess== number:
        print ("Congratulations YOU WON!!")
        break
    elif guess> number :
        print ("Your guess was too high. Guess a number lower than", guess)

    else:
        print ("Your guess was too low. Guess a number higher than", guess)
    
    chances=chances+1

if chances>5:
    print("YOU LOSE!! The number is ", number)

