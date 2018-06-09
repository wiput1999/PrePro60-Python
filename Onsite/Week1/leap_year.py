""" Leap Year """
def main():
    """ Find leap year or not? """
    year = int(input())

    cyear = year - 543

    if cyear % 4 == 0 and (cyear % 100 != 0 or cyear % 400 == 0):
        print("%d is leap year" %year)
    else:
        print("%d is not leap year" %year)

main()
