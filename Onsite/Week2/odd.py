""" Odd??? """
def main():
    """ Check that number is Odd or not? """
    num = int(input())

    for count in range(0, num + 1):
        if count % 2 == 1:
            print("Odd")
        else:
            print(count)

main()
