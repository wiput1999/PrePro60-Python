""" Calculate from message """
def main():
    """ Calculate by condition """
    str_1 = input()
    str_2 = input()

    if len(str_1) % 2 == 0 and len(str_2) % 2 == 0:
        print(max(len(str_1) ** 2, len(str_2) ** 2))
        print(min(len(str_1) ** 2, len(str_2) ** 2))
    elif len(str_1) % 2 == 1 and len(str_2) % 2 == 1:
        print(max(len(str_1) ** 3, len(str_2) ** 3))
        print(min(len(str_1) ** 3, len(str_2) ** 3))
    else:
        print(abs(len(str_1) ** 4 - len(str_2) ** 4))

main()
