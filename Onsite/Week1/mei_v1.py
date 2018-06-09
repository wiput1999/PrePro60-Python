""" Mei V.1 """
def main():
    """ Calculate damage """
    var_a = int(input())
    var_b = int(input())

    if var_a >= 80:
        if var_a + 75 >= var_b:
            print("Solo_Kill")
        else:
            print(var_a + 75)
    else:
        print(var_a)

main()
