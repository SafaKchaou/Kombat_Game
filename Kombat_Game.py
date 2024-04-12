## Functions
import random

# Handling the hero's name input
def name():
    """
    Prompt the user to enter a hero's name and validate it.

        Returns:
            str: The validated hero's name.
    """
    name = input("Please type your hero's name:")
    while name == "":
        print(("Your name is not valid, please enter again."))
        name = input("Please type your hero's name:")
    return name

# Coin toss module
def coin_toss(name1,name2):
    """
        Perform a coin toss to determine which player starts first.

        Args:
            name1 (str): Name of the first player.
            name2 (str): Name of the second player.

        Returns:
            str: The name of the player who starts first.
        """
    s=random.randint(1,2)
    if s==1:
        return name1
    else:
        return name2
# Calculating the success chance
def success_chance(m):
    """
        Calculate the success chance of an attack based on the attack magnitude.

        Args:
            m (int): The attack magnitude, ranging from 1 to 50.

        Returns:
            int: The success chance of the attack, calculated as 100 minus the attack magnitude.
        """
    c=100-m
    return c

# Determining if an attack is successful or not (using a random module)
def randomly_missing_successing(c):
    """
        Determine if an attack is successful or not based on the success chance.

        Args:
            c (int): The success chance of the attack, calculated by the success_chance function.

        Returns:
            bool: True if the attack is successful, False otherwise.
        """
    r=random.randint(50,99)
    if c<r:
        return False
    else:
        return True



## Main program
# Entering the hero's name
print("___First Hero___")
player_1 = name()

print("___Second Hero___")
player_2 = name()
if player_2 == player_1:
    print(f"{player_1} is taken, please choose another name.")
    player_2 = name()

#Starting the attack
#While loop for the repetition of the game
while True :
    sc1=100
    sc2=100

    first=coin_toss(player_1,player_2)
    print("coin toss result:",first," starts first!")

    if first==player_1:
        second=player_2
    else:
        second=player_1

    p1=first
    p2=second

    print(p1, " " * 100, p2)
    print("HP[", sc1, "]:", "I" * (sc1//2), " " * 45, "HP[", sc2, "]:", "I" * ((sc2)//2))
    #While loop for handling the attack between the two players
    while not ( sc2<1 or sc1<1):

        print("_____",first," Attacks!!_____")

        M=int(input("Choose your attack magnitude between 1 and 50:"))
        while not(1<=M<=50):
            print("The attack magnitude must be between 1 and 50.")
            M = int(input("Choose your attack magnitude between 1 and 50:"))

        if randomly_missing_successing(success_chance(M)):
            if first==p1:
                print(p1, "hits", M, "damage!!!")
                sc2=sc2-M

                print(p1, " " * 100, p2)

                if sc2<1:
                    print("HP[", sc1, "]:", "I" * (sc1 // 2), " " * 45, "HP[ 0 ]:")
                else:
                    print("HP[", sc1, "]:", "I" * (sc1// 2), " " * 45, "HP[", sc2, "]:", "I" * ((sc2) // 2))
            else:
                print(p2, "hits", M, "damage!!!")
                sc1 = sc1 - M

                print(p1, " " * 100, p2)

                if sc1<1:
                    print("HP[ 0 ]:", " " * 45, "HP[", sc2, "]:", "I" * (sc2 // 2))
                else:
                    print("HP[", sc1, "]:", "I" * ((sc1) // 2), " " * 45, "HP[", sc2, "]:", "I" * (sc2 // 2))
        else:
            print("Ooopsy!", first, "missed the attack!")
            print(p1, " " * 100, p2)
            print("HP[", sc1, "]:", "I" * (sc1 // 2), " " * 45, "HP[",sc2, "]:", "I" * ((sc2) // 2))
        x=first
        first=second
        second=x

    #Printing the winner
    print("#" * 100)

    if sc1<1:
        print("#" * 50, p2, "wins", "#" * 50)
    else:
        print("#" * 50, p1 , "wins", "#" * 50)

    print("#" * 100)

    #Asking the player for another round
    answer= input("Do you want to play another round ? :")

    while not(answer == "No" or answer == "no" or answer == "Yes" or answer == "yes"):
        answer= input("Do you want to play another round ? :")

    if answer == "No" or answer == "no":
        print("Thanks for playing! See you again!")
        break