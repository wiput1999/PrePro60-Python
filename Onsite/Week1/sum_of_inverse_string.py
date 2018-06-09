""" Sum of inverse string """
def main():
    """ Find sum ASCII of selected character """
    var_a = input()
    var_b = input()

    var_a = var_a[::-1]
    var_b = var_b[::-1]

    var_c = int(input()) - 1
    var_d = int(input()) - 1

    print(ord(var_a[var_c]) + ord(var_b[var_d]))

main()
