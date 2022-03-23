print("Build your own five-men basketball team by picking a number between 0 and 25. You can't use the same number twice.")
name = input("Enter your name: ").capitalize()
players = ["Flight", "LeBron James", "Michael Jordan", "Kobe Bryant", "Stephen Curry", "Shaquille O'Neal", "Stephen A. Smith",
           "Kyrie Irving", "Kevin Durant", "Chris Paul", "Anthony Davis", "Russell Westbrook", "Giannis Antetokounmpo", "James Harden", "Paul George", "Kawhi Leonard", "Damian Lillard", "Luka Dončić", "Nikola Jokić", "Joel Embiid", "Shannon Sharpe", "Trae Young", "Clay Thompson", "Jimmy Butler", "Skip Bayless", f"{name}"]

firstPlayer = int(
    input("Choose your first player. Pick a number between 0 and 25: "))
while firstPlayer > 25 or firstPlayer < 0:
    print("You need to pick a number between 0 and 25. Please try again.")
    firstPlayer = int(
        input("Choose your first player: "))
    if firstPlayer <= 25 and firstPlayer >= 0:
        break
player1 = players[firstPlayer]
print(f"Your first player is {player1}.")

secondPlayer = int(
    input("Choose your second player, you can't use the same number twice: "))
while secondPlayer > 25 or secondPlayer < 0:
    print("You need to pick a number between 0 and 25. Please try again.")
    secondPlayer = int(
        input("Choose your second player: "))
    if secondPlayer <= 25 and secondPlayer >= 0:
        break
while secondPlayer == firstPlayer:
    print("You can't use the same number twice. Please try again.")
    secondPlayer = int(
        input("Choose your second player: "))
    if secondPlayer != firstPlayer:
        break
player2 = players[secondPlayer]
print(f"Your second player is {player2}.")

thirdPlayer = int(
    input("Choose your third player: "))
while thirdPlayer > 25 or thirdPlayer < 0:
    print("You need to pick a number between 0 and 25. Please try again.")
    firstPlayer = int(
        input("Choose your third player: "))
    if thirdPlayer <= 25 and thirdPlayer >= 0:
        break
while thirdPlayer == firstPlayer or thirdPlayer == secondPlayer:
    print("You can't use the same number twice. Please try again.")
    thirdPlayer = int(
        input("Choose your third player: "))
    if thirdPlayer != firstPlayer and thirdPlayer != secondPlayer:
        break
player3 = players[thirdPlayer]
print(f"Your third player is {player3}.")

fourthPlayer = int(
    input("Choose your fourth player: "))
while fourthPlayer > 25 or fourthPlayer < 0:
    print("You need to pick a number between 0 and 25. Please try again.")
    fourthPlayer = int(
        input("Choose your fourth player: "))
    if fourthPlayer <= 25 and fourthPlayer >= 0:
        break
while fourthPlayer == firstPlayer or fourthPlayer == secondPlayer or fourthPlayer == thirdPlayer:
    print("You can't use the same number twice. Please try again.")
    fourthPlayer = int(
        input("Choose your fourth player: "))
    if fourthPlayer != firstPlayer and fourthPlayer != secondPlayer and fourthPlayer != thirdPlayer:
        break
player4 = players[fourthPlayer]
print(f"Your fourth player is {player4}.")

fifthPlayer = int(
    input("Choose your fifth player: "))
while fifthPlayer > 25 or fifthPlayer < 0:
    print("You need to pick a number between 0 and 25. Please try again.")
    firstPlayer = int(
        input("Choose your fifth player: "))
    if fifthPlayer <= 25 and fifthPlayer >= 0:
        break
while fifthPlayer == firstPlayer or fifthPlayer == secondPlayer or fifthPlayer == thirdPlayer or fifthPlayer == fourthPlayer:
    print("You can't use the same number twice. Please try again.")
    fifthPlayer = int(
        input("Choose your fifth player: "))
    if fifthPlayer != firstPlayer and fifthPlayer != secondPlayer and fifthPlayer != thirdPlayer and fifthPlayer != fourthPlayer:
        break
player5 = players[fifthPlayer]
print(f"Your fifth player is {player5}.")

print(
    f"Your team is made up of {player1}, {player2}, {player3}, {player4}, and {player5}.")
