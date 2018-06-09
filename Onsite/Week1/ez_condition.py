""" Ez Condition """
def main():
    """ Display string under condition """
    str_a = input()
    str_b = input()
    num_a = int(input())
    num_b = int(input())

    if (len(str_a) == num_a) and (len(str_b) == num_b):
        print("Yeah! I got it.")
    elif str_a.isalpha() and str_b.endswith("O"):
        print("OMG! Amazing.")
    else:
        print("You lose.")

main()
