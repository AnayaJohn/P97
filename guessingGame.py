import random

number= random(1-9)
chances= 0
guess= input ("Enter your number: ")

print ("Number Guessing Game")
print ("Guess a Number between (1-9)")
print(guess)

while chances<5:
    if guess== number:
        print ("Congratulations YOU WON!!")
        break
    elif guess> number :
        print ("Your guess was too high. Guess a number lower than", guess)
        print (guess)
        break

    elif guess < number:
        print ("Your guess was too low. Guess a number higher than", guess)
        print (guess)

if chances>5:
    print("YOU LOSE!! The number is ", number)

