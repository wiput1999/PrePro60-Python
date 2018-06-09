""" Count type :3 """
def main():
    """ Count type of character """
    text = input()

    result = [0, 0, 0]

    for char in text:
        if char.isupper():
            result[0] += 1
        elif char.islower():
            result[1] += 1
        elif char.isdigit():
            result[2] += 1

    print("Upper : %d" %result[0])
    print("Lower : %d" %result[1])
    print("Number : %d" %result[2])

main()
