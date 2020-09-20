import random
number = random.randrange(1, 101)
tries = 0
guess = 0

print("This is a number guessing game. You only have 10 tries to guess the correct number.")
print("The number is between 1 and 100.")
print("Are you ready? Let's play!")

# While loop will continue as long as guess is not equal to number and tries are less than 10. 
while guess != number and tries < 10:
# try and except block will check the user's input is valid (numbers only). 
    try:
        guess = int(input("What's your guess? "))
    except NameError:
        print("Please enter only whole numbers.")
        continue
    if guess < number:
        print("That's too low.")
    elif guess > number:
        print("That's too high.")
    tries = tries + 1  
    
    
if guess == number:
    print("Congratulations, you guessed correctly!")
else: 
    print("Sorry you did not get it.")
    print("The correct number was " + str(number) + ".")
    