""" Rewind-DayOfTheWeek """
def main():
    """ Main function """
    day = int(input())
    month = int(input()) - 1
    year = int(input())

    day_count = 0

    month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    for count in range(month):
        day_count += month_date[count]

    for count_year in range(2017, year):
        if count_year % 4 == 0:
            day_count += 366
        else:
            day_count += 365

    day_count += day
    day_count -= 1
    day_count %= 7

    print(week[day_count])

main()
