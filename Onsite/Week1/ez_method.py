""" Ez Method """
def main():
    """ Precess String """
    str_a = input()
    str_b = input()

    if str_a.islower() and str_b.islower():
        print(str_a.upper())
        print(str_b.upper())
    elif str_a.isupper() and str_b.isupper():
        print(str_a.lower())
        print(str_b.lower())
    else:
        print("Python is so Ez")

main()
