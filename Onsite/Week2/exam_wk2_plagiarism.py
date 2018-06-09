""" Plagiarism """
def main():
    """ Find Plagiarism """

    psw = input().lower()

    size_psw = len(psw)

    correct = 0

    for rnd in range(20):
        user = input().lower()

        size_user = len(user)

        if size_psw != size_user:
            if rnd != 19:
                print("Entry Denied")
                continue
            else:
                break

        if psw == user:
            print("System Unlocked")
            correct = 1
            break

        like = 0

        for count in range(size_psw):
            if psw[count] == user[count]:
                like += 1
        if rnd != 19:
            print("Likeness = %d" %like)


    if correct == 0:
        print("System Locked Down")



main()
