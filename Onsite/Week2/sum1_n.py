""" Sum 1 to n """
def main():
    """ Find sum of 1 to n """
    number = int(input())

    result = 0

    for count in range(1, number + 1):
        result += count

    print(result)

main()
