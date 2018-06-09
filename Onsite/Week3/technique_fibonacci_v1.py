""" Fibonancci """
def fibo(num):
    """ Calculate fibonancci """
    if num <= 0:
        return 0
    elif num <= 2:
        return 1
    elif num % 2 == 0:
        half = num // 2
        fn1 = fibo(half)
        fn2 = fibo(half - 1)
        return fn1 * (fn1 + 2 * fn2)
    else:
        nhalf = (num - 1) // 2
        fn1 = fibo(nhalf + 1)
        fn2 = fibo(nhalf)
    return fn1 * fn1 + fn2 * fn2


def main():
    """ Main Function """
    num = int(input())
    result = fibo(num)
    print(result)
main()
