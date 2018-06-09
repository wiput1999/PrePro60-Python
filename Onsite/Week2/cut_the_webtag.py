""" cut The webtag """
def main():
    """ Cut <p></p> out from string """
    text = input()

    if text.startswith("<p>") and text.endswith("</p>"):
        print("%100s" %text[3:len(text) - 4])
    else:
        print("%100s" %text)

main()
