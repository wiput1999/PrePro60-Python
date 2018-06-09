""" [Apply String] - Chess board V2 """
def main():
    """ Draw chess board """
    var_x = int(input())
    var_y = int(input())

    print(" _" * var_y + "\n", ("|" + "_|" * var_y + "\n") * var_x, sep='')

main()
