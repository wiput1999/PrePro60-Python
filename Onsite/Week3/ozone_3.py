""" O-z-o-n-e V3 """
def main():
    """ Print a tree """

    num = float(input())

    num = int(num * 100)

    for count in range(1, num + 1):
        print(" " * (num - count) + "* " * count)

    print(" " * (num - 2) + "* *")
    print(" " * (num - 2) + "* *")
    print(" " * (num - 3) + "*" * 5)

main()
