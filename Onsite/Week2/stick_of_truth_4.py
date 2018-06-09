""" [Stick of Truth - 4] Sir """
def main():
    """ Convert string by condition """
    text = input().lower()

    value = int(text.count("fat") * 2 + text.count("big"))

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char.isalpha():
            print(alphabets[int((alphabets.index(char) + value) % 26)], end='')
        else:
            print(char, end='')

main()
