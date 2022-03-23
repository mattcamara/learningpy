# chekc in ideas.txt

""" Requirements for a password
At least 8 characters—the more characters, the better. x
A mixture of both uppercase and lowercase letters. x
A mixture of letters and numbers. x
Inclusion of at least one special character/symbol x

 Requirements for a username
must be at least five characters long x
start with a letter. # Add a featdure that tells users that can't use a certain character like (),{},[],'' .  ect. in there username and passowrd

check for symbools that are not allowed
Only letters and numbers can be used; no special characters, spaces nor symbols (except periods and underscores).
"""
import re
check1 = re.compile('[abcdefghijklmnopqrstuvwxyz]')
check2 = re.compile('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')
check3 = re.compile('[!#$%&*@?^=+_]')  # allowed in password
check3b = re.compile('[~!#$%&*@?^=+-;:`|,]')  # not allowed in username
check4 = re.compile('[0123456789]')
check5 = re.compile('[`~[]()-{}\|/.;:,]')  # not allowed in password
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Your username needs to be at least 5 characters long and must contain only letters, numbers, periods, and underscores. You can't include symbols or other punctuation marks as a part of your username. ")
username = input("Create username: ")
while len(username) < 5:
    print("You need to have at least 5 characters in your username. Please try again.")
    username = input("Re-enter username: ")
    if len(username) >= 5:
        break
while username[0] in numbers:
    print("Username can't start with a number. Please try again.")
    username = input("Re-enter username: ")
    if username[0] not in numbers:
        break
while (check3b.search(username) == None):
    break

else:
    print("You can't include symbols or other punctuation marks as a part of your username except for underscores and periods. Please try again.")
    username = input("Re-enter username: ")

'''print("Your password needs to be at least 8 characters long, a mixture of both uppercase and lowercase letters, a mixture of letters and numbers, and it must contain at least one special character/symbol (!#$%&*@?^=+_).")
password = input("Create password: ")'''
'''while len(password) < 8:
    print("You need to have at least 8 characters in your password. Please try again.")
    password = input("Re-enter password: ")
    if len(password) >= 8:
        break
while (check1.search(password) == None):
    print("You need at least one lowercase letter. Please try again.")
    password = input("Re-enter password: ")
    if (check1.search(password)):
        break
while (check2.search(password) == None):
    print("You need at least one uppercase letter. Please try again.")
    password = input("Re-enter password: ")
    if (check2.search(password)):
        break
while (check3.search(password) == None):
    print("You need at least one of these symbols: (!#$%&*@?^=+_). Please try again.")
    password = input("Re-enter password: ")
    if (check3.search(password)):
        break

while (check4.search(password) == None):
    print("You need at least one number. Please try again.")
    password = input("Re-enter password: ")
    if (check4.search(password)):
        break'''

'''confirm_password = input("Confirm password: ")
while confirm_password != password:
    print("Passwords must be the same. Please try again.")
    confirm_password = input("Confirm password: ")
    if confirm_password == password:
        break
print("You have a strong passowrd.")'''


# useful links:
'''
https://www.youtube.com/watch?v=mG3aGgFYJSE
'''
