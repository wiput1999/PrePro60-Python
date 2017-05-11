""" Card Maker Problem """
def main():
    """ Main Function """
    sender = input()
    receiver = input()
    line_1 = input()
    line_2 = input()

    print("**************************************************")
    print("*                                                *")
    print("*  Hi ", receiver, " " * (43 - len(receiver)), "*", sep='')
    print("*  ", line_1, " " * (46 - len(line_1)), "*", sep='')
    print("*  ", line_2, " " * (46 - len(line_2)), "*", sep='')
    print("*                                                *")
    print("*                                       Thanks,  *")
    print("*", " " * (46 - len(sender)), sender, "  *", sep='')
    print("*                                                *")
    print("**************************************************")


main()
