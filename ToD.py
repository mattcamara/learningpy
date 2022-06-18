
import random

truth = ["What's a bad habit you have?", "Who do you dislike the most in this room?", "What was the last thing you ever stole?",
         "What was the last thin you lied about?", "Who do you find most attractive in this room?"]

dare = ["Read out loud your 5 most recent text messages.", "Show your search history.", "Show an embarrassing picutre of yourself.",
        "Give someone in this room your mom's phone number.", "Let someone draw something on your forehead."]

print("Truth (T) or Dare (D)?")
answer = input(": ").capitalize()

random_truth = random.choice(truth)
random_dare = random.choice(dare)

if answer == "Truth":
    print(random_truth)

if answer == "Dare":
    print(random_dare)
