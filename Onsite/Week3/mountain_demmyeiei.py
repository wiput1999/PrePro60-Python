""" Mountain Demmyeiei """
def main():
    """ Main function """
    num = float(input())

    num = int(num)

    for cnt in range(num):
        print((" " * (num - cnt - 1)) + ("*" * (cnt * 2 + 1)), end='')
        print(((" " * ((num - cnt) * 2 - 1)) + ("*" * (cnt * 2 + 1))) * (num - 1))

main()
