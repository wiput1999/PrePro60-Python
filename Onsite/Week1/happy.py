""" Happy """
def main():
    """ Print string by condition """
    string = input()

    if string[-1].isdigit() or (len(string) == 1 and string[-1].isdigit()):
        print(("%s%s\n" %(string[-1], string)) * 15)
    else:
        if string[0] in "AEIOUaeiou":
            print(("%s\n" %string[::-1]) * 69)
        else:
            print(("%s\n" %string) * 96)

main()
