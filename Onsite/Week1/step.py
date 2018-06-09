""" step """
def main():
    """ Print step """
    string = input()
    var_a = int(input()) - 1
    var_b = int(input()) * 2 + var_a

    print(string[var_a:var_b:2])

main()
