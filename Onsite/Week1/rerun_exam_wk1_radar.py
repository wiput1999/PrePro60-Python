""" [Rerun Exam Week 1] - Radar overlapping v.1 """
def main():
    """ Find radar interception """
    x_1 = float(input())
    y_1 = float(input())
    rad_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())
    rad_2 = float(input())

    distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

    if rad_1 + rad_2 < distance:
        print("No")
    else:
        print("Yes")

main()
