""" Hardcore - The "screen" series - Aligning """
def main():
    """ Draw screen """
    width = int(input())
    height = int(input())
    line = int(input())
    align = input()
    text = input()

    top = line - 1
    bottom = height - top - 3
    space = width - 2

    if len(text) > space:
        print("!!!ERROR!!!")
    elif width < 3 or height < 3:
        print("!!!ERROR!!!")
    elif line > (height - 2):
        print("!!!ERROR!!!")
    elif line <= 0:
        print("!!!ERROR!!!")
    else:
        if align == "center":
            blank = int(((space - len(text)) / 2))
            if (space - len(text)) % 2 == 0:
                string = (" " * blank) + text + (" " * (blank)) + "|"
            else:
                string = (" " * blank) + text + (" " * (blank + 1)) + "|"
            print("-" * width)
            print(("|" + " " * (width - 2) + "|\n") * top, end='')
            print("|" + string)
            print(("|" + " " * (width - 2) + "|\n") * bottom, end='')
            print("-" * width)
        elif align == "left":
            blank = space - len(text)
            string = text + (" " * (blank)) + "|"
            print("-" * width)
            print(("|" + " " * (width - 2) + "|\n") * top, end='')
            print("|" + string)
            print(("|" + " " * (width - 2) + "|\n") * bottom, end='')
            print("-" * width)
        elif align == "right":
            blank = space - len(text)
            string = (" " * (blank)) + text + "|"
            print("-" * width)
            print(("|" + " " * (width - 2) + "|\n") * top, end='')
            print("|" + string)
            print(("|" + " " * (width - 2) + "|\n") * bottom, end='')
            print("-" * width)
        else:
            print("!!!ERROR!!!")

main()
