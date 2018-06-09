""" Domino Pizza """
def main():
    """ Calculate Pizza box amount """
    pizza = int(input())

    bigbox = pizza // 12
    pizza -= (bigbox * 12)
    medbox = pizza // 9
    pizza -= (medbox * 9)
    smallbox = pizza // 6
    pizza -= (smallbox * 6)

    if pizza > 0:
        smallbox += 1

    print("%d / %d / %d" %(bigbox, medbox, smallbox))

main()
