""" Surrender Early game #1 """
def main():
    """ Convert hr:mm to minutes """
    time = input().split(':')

    converted_time = [int(value) for value in time]

    minute = 0

    minute += converted_time[0] * 60
    minute += converted_time[1]

    print(minute)

main()
