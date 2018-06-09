""" Lets Fresh It!! """
def main():
    """ Calculate days and display status """

    number = input().split(' ')

    number = [int(num) for num in number]

    days = 0

    while True:
        min_num = min(number)

        if min_num == 0 and number.count(0) < 4:
            min_num = 1

        min_index = number.index(min(number))

        for num in range(4):
            if num != min_index and number[num] != 0:
                number[num] -= 1

        days += 1

        if min_num == 0:
            print(days)
            break

main()
