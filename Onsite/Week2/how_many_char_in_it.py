""" How many char in it?? V.1 """
def main():
    """ Separate char count """

    text = input()

    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = {}


    # loop in alphabets to proof that sorted
    for alpha in alphabets:
        result[alpha] = 0
        for char in text:
            if char == alpha:
                result[alpha] += 1

    # Loop to check that all index value is 0
    if all([val == 0 for val in result.values()]):
        print("\\@#!$#'\\\\\"$!%&{\"")
    # Print it by index if it not zero
    else:
        for alpha in alphabets:
            if result[alpha] > 0:
                print("%s : %s" %(alpha, result[alpha]))

main()
