""" 12 to 24 """
def main():
    """ Convert 12 to 24 time system """
    hour = int(input())
    minute = int(input())
    period = input()

    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0

    print("24 Hours time is %02d : %02d" %(hour, minute))

main()
