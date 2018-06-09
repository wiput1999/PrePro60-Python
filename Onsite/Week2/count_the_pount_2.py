""" Count the point V.2 """
def add_dot(num, dec):
    """ Add decimal into number """
    result = ""
    times = 0
    num = "0" * dec + num
    while times <= len(num):
        if float(num) == 0:
            result = "0.0"
            break
        if times == len(num) - dec:
            result += "."
        elif times > len(num) - dec:
            result += num[times - 1]
        else:
            result += num[times]
        times += 1
    if result.startswith("0"):
        result = result.lstrip("0")
    if result.startswith("."):
        result = "0" + result
    if result.endswith("."):
        result += "0"

    return result
def remove_dot(num):
    """ Remove dot """
    if float(num) == 0:
        dec = 0
    elif "." in num:
        num = num.strip("0")
        dec = len(num[num.index(".") + 1::1])
    else:
        num = num.lstrip("0")
        dec = 0

    num = num.replace(".", "")

    return int(num), int(dec)

def main():
    """ Calculate specific index """
    num = int(input())

    numbers = []

    for _ in range(num):
        numbers.append(input())

    index = input().split()

    index1, index2 = int(index[0]) - 1, int(index[1]) - 1

    num1, num2 = numbers[index1], numbers[index2]

    num1, dec1 = remove_dot(num1)
    num2, dec2 = remove_dot(num2)

    num = num1 * num2
    dec = dec1 + dec2
    num = add_dot(str(num), dec)

    print(num)

main()
