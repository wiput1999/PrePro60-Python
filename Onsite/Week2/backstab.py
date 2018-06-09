""" Backstab """
def main():
    """ Calculate damage and remaining health """

    deg_1 = float(input())
    deg_2 = float(input())
    health = float(input())

    diff = deg_1 - deg_2

    if diff < 0:
        diff += 360
    if diff < 45:
        diff = 0
    elif diff > 180:
        diff = 360 - diff
        if diff < 45:
            diff = 0


    damage = int(diff * 5) + 50
    result = max(0, int(health - damage))

    print("Remaining Health : %d" %result)
    if result == 0:
        print("Owned!!!")

main()
