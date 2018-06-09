""" What is it """
def main():
    """ Loop until a = b """
    num_a = int(input())
    num_b = int(input())

    while num_a != num_b:
        num_b = int(input())

    print("This is it! %d" %num_b)

main()
