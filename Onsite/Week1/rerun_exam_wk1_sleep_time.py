""" [Rerun Exam Week 1] - Sleep Time """
def main():
    """ Calculate Sleep time """
    sleep_hr = int(input())
    sleep_min = int(input())
    wake_hr = int(input())
    wake_min = int(input())

    result_min = wake_min - sleep_min
    result_hr = wake_hr - sleep_hr

    if result_hr <= 0:
        result_hr += 24

    if result_hr == 24:
        result_hr -= 24

    if result_min < 0:
        result_hr -= 1
        result_min *= -1

        result_min = 60 - result_min

    print("%d:%02d" %(result_hr, result_min))

main()
