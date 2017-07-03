""" Rewind-CharacterCount """
def main():
    """ Main function """
    sentence = input()
    without_space = len(sentence.replace(' ', ''))
    with_space = len(sentence)
    word = len(sentence.split(' '))

    print(without_space, with_space, word)

main()
