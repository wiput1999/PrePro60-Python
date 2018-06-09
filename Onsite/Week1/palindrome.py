""" palindrome """
def main():
    """ Find out palindrome """
    string = input()

    if string == string[::-1]:
        print("%s is Palindrome." %string)
    else:
        print("This is not Palindrome")

main()
