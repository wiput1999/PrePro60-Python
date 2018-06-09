""" %s """
def main():
    """ Display string """
    text = input()
    print("|%s|" %(text))
    print("|%10s|" %(text))
    print("|%-10s|" %(text))
    print("|%.1s %.3s %.5s|" %(text, text, text))

main()
