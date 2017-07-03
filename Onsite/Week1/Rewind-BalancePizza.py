""" Rewind-BalancePizza """
import math

def main():
    """ Main Function """
    pizza_weight = input().split(',')

    pizza_weight = [int(value) for value in pizza_weight]

    pizza_weight = sum(pizza_weight)

    pizza_weight /= 300

    pizza_weight = math.ceil(pizza_weight)

    print(pizza_weight)

main()
