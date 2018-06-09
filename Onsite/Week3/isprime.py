""" Is Prime Number """
def isprime(num):
    """ Calculate isPrime or not?? """
    if num == 1:
        return "No"
    for count in range(2, int(num ** 0.5) + 1):
        if num % count == 0:
            return "No"
    return "Yes"
def main():
    """ Main function """
    num = int(input())

    result = isprime(num)

    print(result)

main()
