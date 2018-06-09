""" [Stick of Truth - 3] Fart Ro Duh """
def main():
    """ Calculate energy and display condition """
    energy = int(input())
    name = input()
    damage = int(input())
    symbol = input()

    if name.count("prad") == 0:
        damage /= 2

    symbol = symbol * round(damage / 1000)

    if energy < 120:
        energy += (name.count("prad") * 10)

        if energy >= 120:
            name = name.replace("prad", "")

            print("Skill: %s" %name)
            print("%s" %symbol)
            print("%.2f" %(damage / 1000))
            print("Douchebag")
        else:
            print("%_\\\\ Noob Douchebag //_%")
    else:
        print("Skill: %s" %name)
        print("%s" %symbol)
        print("%.2f" %(damage / 1000))
        print("Douchebag")

main()
