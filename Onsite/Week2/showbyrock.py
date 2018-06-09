""" ShowbyRock """
def main():
    """ Display result of the game by condition """
    player1 = input()
    player2 = input()

    if player1 == player2:
        print("Banabana")
    elif player1 == "Rock":
        if player2 == "Scissors":
            print("God of Banana")
        elif player2 == "Paper":
            print("Banabird")
    elif player1 == "Scissors":
        if player2 == "Rock":
            print("Banabird")
        elif player2 == "Paper":
            print("God of Banana")
    elif player1 == "Paper":
        if player2 == "Scissors":
            print("Banabird")
        elif player2 == "Rock":
            print("God of Banana")

    if player1 == "Rock":
        print("Rock!!!")

main()
