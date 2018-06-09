""" Count the point V.1 """
def main():
    """ Count decimal """
    num = int(input())

    for _ in range(num):
        number = input()

        index = number[::-1].find('.')

        if index == -1:
            print(0)
        else:
            print(index)

main()
