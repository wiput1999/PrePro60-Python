""" %d """
def main():
    """ Display string """
    text = int(input())
    print("|%d|" %(text))
    print("|+%d|" %(text))
    print("|%10d|" %(text))
    print("|%-10d|" %(text))
    print("|%05d|" %(text))

main()
