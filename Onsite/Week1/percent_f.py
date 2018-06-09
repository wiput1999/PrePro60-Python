""" %d """
def main():
    """ Display string """
    text = float(input())
    print("|%.2f|" %(text))
    print("|+%.2f|" %(text))
    print("|%10.2f|" %(text))
    print("|%-10.2f|" %(text))
    print("|%010.2f|" %(text))

main()
