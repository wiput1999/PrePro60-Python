""" Max, Mean, Min """
def main():
    """ Main function """
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())

    print("Max:", max(var1, var2, var3))
    print("Mean:", round((var1 + var2 + var3) / 3))
    print("Min:", min(var1, var2, var3))

main()
