""" Rewind-BankNoteCount """
def main():
    """ Main function """
    money = int(input())

    # Note 1000
    note_1000 = money // 1000
    money -= (note_1000 * 1000)

    # Note 500
    note_500 = money // 500
    money -= (note_500 * 500)

    # Note 100
    note_100 = money // 100
    money -= (note_100 * 100)

    if money % 20 != 0:
        # Note 50
        note_50 = money // 50
        money -= (note_50 * 50)
    else:
        note_50 = 0

    # Note 20
    note_20 = money // 20
    money -= (note_20 * 20)

    if money == 0:
        print(note_20 + note_50 + note_100 + note_500 + note_1000)
    else:
        print(0)

main()
