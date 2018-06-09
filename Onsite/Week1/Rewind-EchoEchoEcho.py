""" Rewind-EchoEchoEcho """
def main():
    """ Main function """
    text = input()

    char_count = 999999
    word = ""

    for char in text:
        char_count = min(text.count(char), char_count)

    for char in range(int(len(text) / char_count)):
        word += text[char]

    print(word, char_count, "time")

main()
