""" Calculate password score """
def calculate(password):
    """ Calculate and Print Result """
    score = 0
    if password.isdigit() is True:
        score += 50

    if password.isalpha() is True:
        score += 30

    if password.islower() is True and password.isalpha() is True:
        score += 100

    if password.isupper() is True and password.isalpha() is True:
        score += 85

    psw = password
    sec = psw.isdigit() is False and psw.isalpha() is False and psw.swapcase() != psw
    if sec:
        score += 75

    if password.islower() is False and password.isupper() is False and password.isalpha() is True:
        score += 175

    if password.count(password[0]) >= 5:
        score -= (password.count(password[0]) - 4) * 15

    if len(password) > 10:
        score += (len(password) - 10) * 10

    score += ord(password[-1])

    if score <= 150:
        security = "poor"
    elif score <= 300:
        security = "acceptable"
    else:
        security = "secure"

    print("Password : " + "*" * len(password))
    print("Security score : %d" %score)
    print("Security level : %s" %security)

def main():
    """ Calculate password score """
    password = input()

    if len(password) < 6:
        print("try again")
        password = input()
        if len(password) >= 6:
            calculate(password)
        else:
            print("process terminated")
    else:
        calculate(password)

main()
