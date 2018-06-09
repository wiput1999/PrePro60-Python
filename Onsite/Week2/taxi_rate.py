""" Taxi Rate """
def main():
    """ Calculate Taxi price """
    distance = int(input())
    time = int(input())

    price = 50

    # 0 - 1
    distance -= 1

    # 2 - 10
    if distance > 0:
        price += min(distance * 5, 45)
        distance -= 9

    # 11 - 20
    if distance > 0:
        price += min(distance * 7.5, 75)
        distance -= 10

    # 21 - 40
    if distance > 0:
        price += min(distance * 10, 200)
        distance -= 20

    # 41 - 65
    if distance > 0:
        price += min(distance * 12.5, 312.5)
        distance -= 25

    # 65 ++
    if distance > 0:
        price += distance * 15


    new_time = time // 60

    if time % 60 != 0:
        new_time += 1

    price += new_time * 1.5

    if price % 1 != 0:
        price -= price % 1
        price += 1

    print(int(price))

main()
