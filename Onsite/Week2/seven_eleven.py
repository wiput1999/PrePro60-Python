""" Seven Eleven """
def main():
    """ Calculate achievement """
    employee = input()
    rice = int(input())
    sandwich = int(input())
    sarapao = int(input())
    drink = int(input())
    snack = int(input())

    achievement = ""

    if rice >= 25:
        rice *= 2
        achievement += "R "

    if sandwich >= 40:
        sandwich *= 2
        achievement += "S "

    if sarapao >= 70:
        sarapao *= 2
        achievement += "P "

    if drink >= 100:
        drink *= 2
        achievement += "W "

    if snack >= 250:
        snack *= 2
        achievement += "K "

    payday = rice * 30 + sandwich * 25 + sarapao * 20 + drink * 15 + snack * 10

    print("Employee : %s" %employee)
    print("Payday : %d Baht." %payday)
    print("Archivement : %s" %achievement)
    print("You did great!, %s." %employee)

main()
