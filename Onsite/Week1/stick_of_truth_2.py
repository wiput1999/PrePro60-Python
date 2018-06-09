""" [Stick of Truth - 2] Go or not """
def main():
    """ Calculate that can go or not """
    # Unit in meters
    distance = int(input())
    bread = int(input())
    water = int(input())
    strength = int(input())
    width = int(input())

    strength += (bread * 2 + water)

    # Not Go
    if distance >= (strength * 1200):
        notgo = int((width -8) / 2)
        if width % 2 == 0:
            string = "#" + " " * notgo  + "Not Go" + " " * notgo + "#"
            print("#" * width)
            print(string)
            print("#" * width)
        else:
            string = "#" + " " * notgo + "Not Go" + " " * (notgo + 1) + "#"
            print("#" * width)
            print(string)
            print("#" * width)
    # Can Go
    else:
        cango = int((width - 4) / 2)
        if width % 2 == 0:
            string = "#" + " " * cango  + "Go" + " " * cango + "#"
            print("#" * width)
            print(string)
            print("#" * width)
        else:
            string = "#" + " " * cango + "Go" + " " * (cango + 1) + "#"
            print("#" * width)
            print(string)
            print("#" * width)

main()
