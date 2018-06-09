""" [Rerun Exam Week 1] - Weapon """
def main():
    """ Specifiy type of gun by sound """

    sound = input()

    pew = sound.count("pew")

    if (pew % 2 == 0 and pew > 0 and pew < 6) or pew == 1:
        print("Semi-Automatic")
    elif pew >= 3:
        print("Automatic")
    else:
        print("Safe")

main()
