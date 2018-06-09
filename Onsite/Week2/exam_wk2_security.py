""" Security Level """
def security(password):
    """ calculate security level """

    if password.isalnum() and len(password) >= 6:
        result = [0, 0, 0]
        for char in password:
            if char.isupper():
                result[0] += 1
            elif char.islower():
                result[1] += 1
            elif char.isdigit():
                result[2] += 1

        pass_count = 0
        if result[0] > 0:
            pass_count += 1
        if result[1] > 0:
            pass_count += 1
        if result[2] > 0:
            pass_count += 1

        if pass_count == 1:
            return "Security-Level: Low"
        elif pass_count == 2:
            return "Security-Level: Medium"
        elif pass_count == 3:
            return "Security-Level: High"

    return "Invalid"

def main():
    """ Security Level calculate """

    num = int(input())

    for _ in range(num):
        data = input()

        username, pwd = data.split(' ')

        print("Username: %s / Password: %s (%s)" %(username, "*" * len(pwd), security(pwd)))


main()
