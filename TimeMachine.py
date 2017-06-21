""" Time Machine """
def main():
    """ Main function """
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    current = input()
    dur = int(input())

    ind = month.index(current)

    res = (ind + dur) % 12

    if res < 0:
        res *= -1

    print(month[res])

main()
