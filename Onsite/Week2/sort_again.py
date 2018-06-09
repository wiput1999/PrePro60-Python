""" Sort again """
def main():
    """ Sort n numbers """
    num = int(input())

    numbers = list()

    for _ in range(num):
        numbers.append(float(input()))

    for number in sorted(numbers):
        print("%g" %number, end=' ')

main()
