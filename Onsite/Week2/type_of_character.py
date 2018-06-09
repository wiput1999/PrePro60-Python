""" Type of character """
def main():
    """ Find type of character """
    string = input()

    for char in string:
        if char.isupper():
            print("%s is uppercase letter" %char)
        elif char.islower():
            print("%s is lowercase letter" %char)
        elif char.isdigit():
            print("%s is number" %char)

main()
