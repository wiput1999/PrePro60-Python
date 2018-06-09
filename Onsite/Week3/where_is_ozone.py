""" Where is Ozone """
def main():
    """ Main Function """
    num = int(input())

    print(" " * (num - 1) + "*")
    for cnt in range(num - 1):
        print(" " * (num - cnt - 2), end='')
        print("*" + " " * cnt + "*" + " " * cnt + "*")
    for cnt in range(3):
        print(" " * (num - 1) + "*")
main()
