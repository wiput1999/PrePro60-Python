""" My Money """
def main():
    """ Calculate Money in the pocket """

    name = input()

    total = 0

    while True:
        command = input()

        if command == "deposit":
            money = int(input())
            total += money
        elif command == "withdraw":
            money = int(input())
            total -= money
        elif command == "delete":
            total = 0
        elif command == "Stop":
            print("%s : %d" %(name, total))
            break


main()
