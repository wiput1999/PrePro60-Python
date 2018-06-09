""" Final Fantastic """
def main():
    """ Display screen with condition """

    damage = int(input())
    boss = input()
    boss_size = int(input())
    skill = int(input())

    if boss_size % 2 != 0:
        boss_size += 1

    boss *= boss_size

    tackle = ""
    iron = ""
    growl = ""
    flash = ""


    if skill == 1:
        tackle = ">"
    if skill == 2:
        iron = ">"
    if skill == 3:
        growl = ">"
    if skill == 4:
        flash = ">"


    print("o--------------------o")
    print("|%-20.07d|" %damage)
    print("|%20s|" %boss.center(20))
    print("|%20s|" %boss.center(20))
    print("|%20s|" %boss.center(20))
    print("|____________________|")
    print("|%2sTackle%2sIron tail |" %(tackle, iron))
    print("|%2sGrowl%3sFlash     |" %(growl, flash))
    print("o--------------------o")

main()
