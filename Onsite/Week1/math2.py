""" Math 2 """
def main():
    """ Main function """
    var_a = int(input())
    var_b = int(input())

    var_d = 250
    var_e = (125 * var_a + var_b) / 2
    var_f = ((var_e - var_a) * var_b) + var_d

    var_c = var_a + var_b + var_d + var_e + var_f

    print(var_c)

main()
