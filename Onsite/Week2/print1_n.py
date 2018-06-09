""" Print (1 to n) """
def main():
    """ Print 1 to n in the same line """
    number = int(input())

    for count in range(1, number + 1):
        print(count, end='')

main()
