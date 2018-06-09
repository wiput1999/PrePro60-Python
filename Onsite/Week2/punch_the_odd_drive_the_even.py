""" Punch the Odd, Drive the Even """
def main():
    """ Calculate odd even by condition """
    number = int(input())

    while number >= 1:
        if number % 2 == 1 and number != 1:
            print(int(number), end=' ')
            number += 1
        else:
            print(int(number), end=' ')
            number /= 2

main()
