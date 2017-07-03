""" Rewind-BankNoteValue """
def main():
    """ Main function """
    result = 0
    result += (int(input()) * 1000)
    result += (int(input()) * 500)
    result += (int(input()) * 100)
    result += (int(input()) * 50)
    result += (int(input()) * 20)

    print(result)

main()
