""" O_Z_o_n_e V(5-1) """
def add(amount, product):
    """ Add amount by product """
    if product == "Chang":
        quantity = int(input())
        amount["Chang"] += quantity
    elif product == "Leo":
        quantity = int(input())
        amount["Leo"] += quantity
    elif product == "Singha":
        quantity = int(input())
        amount["Singha"] += quantity
    elif product == "Heineken":
        quantity = int(input())
        amount["Heineken"] += quantity
    elif product == "Ice":
        quantity = int(input())
        amount["Ice"] += quantity

    return amount
def main():
    """ Calculate price by product with condition """

    amount = {
        "Chang" : 0,
        "Leo" : 0,
        "Singha" : 0,
        "Heineken": 0,
        "Ice" : 0
    }

    result = {}

    while True:
        product = input()

        amount = add(amount, product)


        if product == "OK":
            break

    for product in sorted(amount):
        if amount[product] > 0:
            if product == "Chang":
                result[product] = 0
                result[product] += (80 * (amount[product] % 5))
                result[product] += (75 * max(amount[product] - (amount[product] % 5), 0))
            elif product == "Leo":
                result[product] = 0
                result[product] += (85 * amount[product])
            elif product == "Singha":
                result[product] = 0
                result[product] += (80 * amount[product])
            elif product == "Heineken":
                result[product] = 0
                result[product] += (90 * (amount[product] % 5))
                result[product] += (78 * max(amount[product] - (amount[product] % 5), 0))
            elif product == "Ice":
                result[product] = 25

    for product in sorted(result):
        print("%s\t:\t%d" %(product, result[product]))

main()
