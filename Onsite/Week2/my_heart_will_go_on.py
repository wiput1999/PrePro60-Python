""" My heart will go on """
def main():
    """ Display message by condition """
    text = input()

    while True:
        space = text.find(" ") + 1
        vowel = 0
        digit = 0
        for char in text[space:]:
            if char.isdigit():
                digit += 1
            elif char in "aeiou":
                vowel += 1

        if digit > 0 or vowel > 0:
            text = input()
        else:
            print(text)
            break

main()
