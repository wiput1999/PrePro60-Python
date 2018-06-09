""" [Rerun Exam Week 1] - Nth Digit (easy) V.En """
def main():
    """ Find nth string """
    string = "123456789101112131415161718192021222324252627282930"

    index = int(input()) - 1

    if index >= len(string):
        print("Out of Range")
    else:
        print(string[index])

main()
