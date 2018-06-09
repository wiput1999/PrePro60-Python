""" salapao """
def main():
    """ Find point that on circle or not? """
    rad_x = float(input())
    rad_y = float(input())
    radius = float(input())
    point_x = float(input())
    point_y = float(input())

    if ((point_x - rad_x) ** 2) + ((point_y - rad_y) ** 2) <= radius ** 2:
        print("Yess!")
    else:
        print("Noo!")

main()
