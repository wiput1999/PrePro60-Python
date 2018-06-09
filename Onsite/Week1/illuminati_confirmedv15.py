""" illuminati confirmedV.1.5 """
def main():
    """ Print pyramid """
    var_a = input()
    var_b = int(input())

    print("%10s" %var_a, sep='')
    print("%9s %s" %(var_a, var_a), sep='')
    print("%8s %s %s" %(var_a, str(abs(var_b)) * 1, var_a), sep='')
    print("%7s %s %s" %(var_a, str(abs(var_b - 1)) * 3, var_a), sep='')
    print("%6s %s %s" %(var_a, str(abs(var_b - 2)) * 5, var_a), sep='')
    print("%5s %s %s" %(var_a, str(abs(var_b - 3)) * 7, var_a), sep='')
    print("%4s %s %s" %(var_a, str(abs(var_b - 4)) * 9, var_a), sep='')
    print("%3s %s %s" %(var_a, str(abs(var_b - 5)) * 11, var_a), sep='')
    print("%2s %s %s" %(var_a, str(abs(var_b - 6)) * 13, var_a), sep='')
    print(var_a * 19)
    print("illuminaticonfirmed")

main()
