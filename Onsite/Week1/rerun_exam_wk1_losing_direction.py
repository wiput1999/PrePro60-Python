""" Rerun Exam Week 1 - Losing Direction """
def main():
    """ Check invalid direction """
    direction = input()
    deg_a = int(input())
    deg_b = int(input())
    deg_c = int(input())
    deg_d = int(input())

    if direction == "N":
        deg_init = 0
    elif direction == "E":
        deg_init = 90
    elif direction == "S":
        deg_init = 180
    elif direction == "W":
        deg_init = 270

    if (deg_a + deg_b + deg_c + deg_d) % 90 != 0:
        print("Error")
    else:
        deg_init += (deg_a + deg_b + deg_c + deg_d)

        deg_init %= 360

        if deg_init == 0:
            print("N")
        elif deg_init == 90:
            print("E")
        elif deg_init == 180:
            print("S")
        elif deg_init == 270:
            print("W")

main()
