""" [Rerun Exam Week 1] - Area where circle and square lies on """
def main():
    """ Find area """
    diameter = int(input())

    radius = diameter / 2

    area = diameter ** 2 - (22/7) * radius ** 2

    area /= 4

    print("%.2f" %area)

main()
