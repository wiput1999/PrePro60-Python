""" Multitable """
def main():
    """ Print multitable """
    number = int(input())

    for count in range(1, 13):
        print("%d X %-3d= %d" %(number, count, number * count))

main()
