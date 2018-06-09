""" Spread it """
def main():
    """ Sort by index """

    text = input()

    result = {}

    amount = []

    for char in text:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    print(sorted(result.keys(), reverse=True))

    for data in sorted(result.keys(), reverse=True):
        amount.append(result[data])

    print(amount)


main()
