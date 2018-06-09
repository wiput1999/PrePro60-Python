""" While """
def main():
    """ Count how many time that loop operate """
    num_a = int(input())
    num_b = int(input())

    count = 0

    while num_a <= num_b:
        num_a += 1
        count += 1

    print(count)

main()
