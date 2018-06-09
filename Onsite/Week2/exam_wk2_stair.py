""" Climbing Stairs """
def main():
    """ Count how to climb Stairs """

    num = int(input())

    result = [1, 2, 3]

    for count in range(3, num):
        temp = result[count - 1] + result[count - 2]
        result.append(temp)

    print(result[len(result) - 1])


main()
