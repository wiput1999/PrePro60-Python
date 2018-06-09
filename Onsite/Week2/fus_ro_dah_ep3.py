""" [Intermidate]Fus ro Dahhh!!!! The series Ep.3 """
def main():
    """ Calculate days and display status """

    number = input().split(' ')

    number = [int(num) for num in number]

    days = 0

    while True:
        min_num = min(number)

        if min_num == 0:
            print(days)
            break

        min_index = number.index(min(number))

        for num in range(4):
            if num != min_index:
                number[num] -= 1

        for num in number:
            print(num, end=' ')
        print()

        days += 1

main()
