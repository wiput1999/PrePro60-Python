""" Sorting Number """
def third(num_1, num_2, num_3, num_4):
    """ Find 3rd maximum """
    maximum = max(num_1, num_2, num_3, num_4)
    minimum = min(num_1, num_2, num_3, num_4)
    temp = minimum
    if num_1 != minimum and num_1 != maximum:
        if num_1 > temp:
            temp = num_1
    if num_2 != minimum and num_2 != maximum:
        if num_2 > temp:
            temp = num_2
    if num_3 != minimum and num_3 != maximum:
        if num_3 > temp:
            temp = num_3
    if num_4 != minimum and num_4 != maximum:
        if num_4 > temp:
            temp = num_4

    return temp

def second(num_1, num_2, num_3, num_4):
    """ Find 2nd maximum """
    maximum = max(num_1, num_2, num_3, num_4)
    minimum = min(num_1, num_2, num_3, num_4)
    temp = third(num_1, num_2, num_3, num_4)
    if num_1 != minimum and num_1 != maximum:
        if num_1 < temp:
            temp = num_1
    if num_2 != minimum and num_2 != maximum:
        if num_2 < temp:
            temp = num_2
    if num_3 != minimum and num_3 != maximum:
        if num_3 < temp:
            temp = num_3
    if num_4 != minimum and num_4 != maximum:
        if num_4 < temp:
            temp = num_4

    return temp

def main():
    """ Display sorted number """
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())

    maximum = max(num_1, num_2, num_3, num_4)
    minimum = min(num_1, num_2, num_3, num_4)

    print(minimum)
    print(second(num_1, num_2, num_3, num_4))
    print(third(num_1, num_2, num_3, num_4))
    print(maximum)

main()
