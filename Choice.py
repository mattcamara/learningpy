print("Welcome to Choice!")

name = input("What is your name? ")
age = int(input("How old are you? "))
health = 5


if age >= 15:
    print(name + ", " "you are old enough to play the game.")
    start = input("Do you want to start? ").lower()
    if start == "yes":
        print("Great, let's begin!")
        print("You are starting with 5 health.")
        ans = input(
            "Do you want to take the right or left path (left/right)? ").lower()
        if ans == "left":
            print("The path you choose lead you to a lake.")
            ans = input(
                "Do you want to swim across or go around the lake (across/around)? ").lower()
            if ans == "around":
                print("You were able to get around the lake and reach the other side.")
            elif ans == "across":
                print(
                    "You managed to swim across the lake and reached the other side but got attacked by an alligator, losing 3 health.")
                health -= 3
                print("You are now at", health, "health.")
            print("On the other side of the lake you find an egg on the ground. Above the egg, there's a nest in a tree.")
            ans = input(
                "Do you climb the tree and put the egg back in the nest or leave the egg on the ground (climb/leave)? ")

            if ans == "climb":
                print("You start climbing the tree but then lose your grip. The egg falls down and cracks and you fall down losing 2 health.")
                health -= 2
                print("You are now at", health, "health.")

                if health <= 0:
                    print("You died. GAME OVER")

                else:
                    ans = input(
                        "You once again come across two paths. Do you take the left or right path (left/right)? ")

                    if ans == "left":
                        print(
                            "Did you really think the answer will be the same twice? You lose. GAME OVER")

                    elif ans == "right":
                        print(
                            "You followed the path which lead you to your home. You win. GAME OVER")

            elif ans == "leave":
                print("You mind your own business and leave the egg on the ground. You feel guilty for leaving the egg and lose 1 health.")
                health -= 1
                print("You are now at", health, "health.")
                ans = input(
                    "You once again come across two paths. Do you take the left or right path (left/right)? ")

                if ans == "left":
                    print(
                        "Did you really think the answer will be the same twice? You lose. GAME OVER")

                elif ans == "right":
                    print(
                        "You followed the path which lead you to your home. You win. GAME OVER")

        else:
            print("The path you choose lead you into a ditch and you died. GAME OVER")

    else:
        print("Well, cya!")

else:
    print("Sorry", name + ", " "you are not old enough to play the game.")
