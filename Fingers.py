guess_number = int(input("How many fingers do I have up? "))
number = 5
if guess_number > 10:
    print("I don't have that many fingers.")
if guess_number <= 0:
    print("Nope.")
while guess_number != number:
    print("Incorrect. Try again.")
    guess_number = int(input("How many fingers do I have up? "))
if number > 8:
    print("You are correct. Game Over.")
    exit()
if guess_number == number:
    print("You are correct.")
continue_ = input("Do you want to continue the game? (Yes)/(No) ").capitalize()
while continue_ == "Yes":
    number += 2
    if number > 10:
        break
    guess_number = int(input("How many fingers do I have up? "))
    if guess_number != number:
        print("Incorrect. Game Over.")
        break
    elif guess_number == number:
        print("You are correct. Game Over.")
        break

else:
    print("Thanks for playing. Game Over.")
