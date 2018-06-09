""" [Rerun Exam Week 1] - Cinema V.1 """
def main():
    """ Calculate ticket price """
    day = input()
    amount = int(input())

    if day == "monday":
        result = amount * 120
    elif day == "tuesday":
        result = amount * 120
    elif day == "wednesday":
        result = amount * 80
    elif day == "thursday":
        result = amount * 140
    elif day == "friday":
        result = amount * 140
    elif day == "saturday":
        result = amount * 140
    elif day == "sunday":
        result = amount * 140

    print(result)

main()
