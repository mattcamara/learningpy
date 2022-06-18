import random
responses = ["Don't count on it", "Yes, definitely", "No", "Yes", "Maybe",
             "Most likely", "Yuh", "Without a doubt", "Probably not", "I don't think so", "Nuh", "Ask again later"]
print("Welcome! I'm Magic 8 Ball. Ask me any quesiton and I will provide you with answers and predictions!")

question = input("Type your question here: ")

random_response = random.choice(responses)
print(random_response)
