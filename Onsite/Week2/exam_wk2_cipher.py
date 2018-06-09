""" Atbash cipher :3 """
def main():
    """ Decrypt string """

    text = input()

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    meaning = "zyxwvutsrqponmlkjihgfedcba"

    for char in text:
        if char.isalpha():
            pos = alphabets.index(char)
            print(meaning[pos], end='')
        else:
            print(char, end='')

main()
