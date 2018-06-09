""" Diamond """
def main():
    """ Draw picture """
    num = int(input())

    for count in range(1, num + 1):
        print(" " * (num - count), "*" * (count * 2 - 1), sep='')
    for count in range(num - 1, 0, -1):
        print(" " * (num - count), "*" * (count * 2 - 1), sep='')

main()
