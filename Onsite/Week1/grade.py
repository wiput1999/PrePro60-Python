""" Grade """
def main():
    """ Calculate grade by condition """
    score = int(input())

    if score <= 49:
        print(0.0)
    elif score <= 54:
        print(1.0)
    elif score <= 59:
        print(1.5)
    elif score <= 64:
        print(2.0)
    elif score <= 69:
        print(2.5)
    elif score <= 74:
        print(3.0)
    elif score <= 79:
        print(3.5)
    else:
        print(4.0)

main()
