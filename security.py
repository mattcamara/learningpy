print("From the list, select two security questions and answer them.")
securityquestions = ["What higschool did you attend?",
                     "What city were you born in?", "What was the first thing you learned to cook?", "What is your mother's maiden name?", "Where did you go the first time you flew on a plane?", "Who was your first kiss?"]


print(securityquestions)


securityq_select = int(input(
    "Choose your first secrutity question by picking a number between 0 and 5: "))
securityq1 = securityquestions[securityq_select]
print(securityq1)
usercorrectanswer1 = input("Answer: ").capitalize()
print("Your answer is saved.")

securityq_select2 = int(input(
    "Choose your second secrutity question by picking a number between 0 and 5: "))
while securityq_select2 == securityq_select:
    print("You can't use the same quesiton. Please try again.")
    securityq_select2 = int(input(
        "Pick a number between 0 and 5: "))
    if securityq_select2 != securityq_select:
        break
securityq2 = securityquestions[securityq_select2]
print(securityq2)
usercorrectanswer2 = input("Answer: ").capitalize()
print("Your answer is saved.")


print("Login")

securityq1_answer = input(f"{securityq1}: ").capitalize()
while securityq1_answer != usercorrectanswer1:
    print("Oops! Answer is incorrect. Please try again.")
    securityq1_answer = input(f"{securityq1}: ").capitalize()
    if securityq1_answer == usercorrectanswer1:
        break
print("Answer is correct.")

securityq2_answer = input(f"{securityq2}: ").capitalize()
while securityq2_answer != usercorrectanswer2:
    print("Oops! Answer is incorrect. Please try again.")
    securityq2_answer = input(f"{securityq2}: ").capitalize()
    if securityq2_answer == usercorrectanswer2:
        break
print("Answer is correct.")
