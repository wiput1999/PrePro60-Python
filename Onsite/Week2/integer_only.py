""" Integer Only """
def main():
    """ Got the value unitl not integer """

    num = input()
    number = list()

    while num.isdigit():
        number.append(int(num))
        num = input()

    count = len(number)
    if count == 0:
        print("Python is very Ez")
    else:
        total = sum(number)
        avg = total / len(number)

        print("Sum of number is %d" %total)
        print("Average is : %.2f" %avg)

main()
