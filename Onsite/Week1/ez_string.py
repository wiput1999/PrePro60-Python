""" Ez String """
def main():
    """ Print String in different pattern """
    str_a = input()
    num_b = int(input())

    print("%s " %str_a * num_b)
    print("%s %s" %(str_a, str(num_b) * num_b))
    print("%s %s" %(str_a, str_a[::-1]))
    print("%s" %str_a[-1:-4:-1])

main()
