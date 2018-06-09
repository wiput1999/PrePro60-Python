""" Hardcore - The "screen" series - Introduction """
def main():
    """ Draw screen """
    width = int(input())
    height = int(input())
    align = int(input())
    line = int(input())
    text = input()

    top = line - 1
    bottom = height - top - 3
    space = width - len(text) - 2

    string = (" " * (space * align)) + text + (" " * (space * align * -1)) + "|"

    print("-" * width)
    print(("|" + " " * (width - 2) + "|\n") * top, end='')
    print("|" + string)
    print(("|" + " " * (width - 2) + "|\n") * bottom, end='')
    print("-" * width)

main()
