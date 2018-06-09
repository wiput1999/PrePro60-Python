""" [Stick of Truth - 1] Time Converter """
def main():
    """ Convert time """
    # Parallel Hour
    para_hr = int(input())
    # Parallel Minute
    para_min = int(input())
    # Parallel Second
    para_sec = int(input())

    pre_result = (para_hr * 50 * 29) + (para_min * 29) + para_sec

    pre_result *= 14

    # Real World Second
    real_sec = pre_result % 60
    pre_result //= 60
    # Real World Minute
    real_min = pre_result % 60
    pre_result //= 60
    # Real World Hour
    real_hr = pre_result % 24
    pre_result //= 24
    # Real World Day
    real_day = pre_result

    print("%02d:%02d:%02d" %(real_hr, real_min, real_sec))
    print("Day : %d" %real_day)

main()
