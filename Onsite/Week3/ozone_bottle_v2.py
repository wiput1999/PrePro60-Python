""" O-Z-o-n-e Bottle V2 """
def main():
    """ Main function """
    num = int(input())

    print(" " * (num - 1) + "*" * num)

    for _ in range(num):
        print(" " * (num - 1) + "*" + " " * (num - 2) + "*")

    for cnt in range(num - 2):
        print(" " * (num - cnt - 2) + "*" + " " * (num + (cnt * 2)) + "*")

    for _ in range(num * 2):
        print("*" + " " * (3 * num - 4) + "*")

    print("*" * (3 * num - 2))

main()
