""" Game of python V.1 """
def check_p1(game):
    """ Check player 1 game status """
    if game["1"] == "x" and ((game["2"] == "x" and game["3"] == "x") or \
        (game["4"] == "x" and game["7"] == "x") or (game["5"] == "x" and game["9"] == "x")):
        return True
    elif game["2"] == "x" and game["5"] == "x" and game["8"] == "x":
        return True
    elif game["3"] == "x" and ((game["6"] == "x" and game["9"] == "x") or \
        (game["5"] == "x" and game["7"] == "x")):
        return True
    elif game["4"] == "x" and game["5"] == "x" and game["6"] == "x":
        return True
    elif game["7"] == "x" and game["8"] == "x" and game["9"] == "x":
        return True
    return False

def check_p2(game):
    """ Check player 2 game status """
    if game["1"] == "o" and ((game["2"] == "o" and game["3"] == "o") or \
        (game["4"] == "o" and game["7"] == "o") or (game["5"] == "o" and game["9"] == "o")):
        return True
    elif game["2"] == "o" and game["5"] == "o" and game["8"] == "o":
        return True
    elif game["3"] == "o" and ((game["6"] == "o" and game["9"] == "o") or \
        (game["5"] == "o" and game["7"] == "o")):
        return True
    elif game["4"] == "o" and game["5"] == "o" and game["6"] == "o":
        return True
    elif game["7"] == "o" and game["8"] == "o" and game["9"] == "o":
        return True
    return False

def print_game(game):
    """ Print Gameboard """
    print("|%s|%s|%s|" %(game["1"], game["2"], game["3"]))
    print("|%s|%s|%s|" %(game["4"], game["5"], game["6"]))
    print("|%s|%s|%s|" %(game["7"], game["8"], game["9"]))
    print()

def main():
    """ Main function to input data to game """

    game = {
        "1": "_",
        "2": "_",
        "3": "_",
        "4": "_",
        "5": "_",
        "6": "_",
        "7": "_",
        "8": "_",
        "9": "_",
        }

    player1_name = input()
    player2_name = input()

    player1, player2 = False, False

    for count in range(9):
        pos = input()
        if count % 2 == 0:
            game[pos] = "x"
        else:
            game[pos] = "o"

        print_game(game)

        player1 = check_p1(game)
        player2 = check_p2(game)

        if player1:
            print(player1_name, "Win!!")
            break

        if player2:
            print(player2_name, "Win!!")
            break

    if player1 is False and player2 is False:
        print("Draw")

main()
