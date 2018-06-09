""" yes no ok thxu """
def main():
    """ Check length of string and display message by condition """
    string = input()

    length = len(string)

    if length <= 3:
        print("Yes")
    elif length <= 10:
        print("No")
    elif length <= 20:
        print("Ok")
    elif length <= 100:
        print("Thank You")
    else:
        print("OMFG To Many For Me GG")

main()
