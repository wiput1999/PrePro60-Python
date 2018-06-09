""" a^n """
def main():
    """ Main Function """
    base = int(input())
    exp = int(input())

    base2 = base
    if base < 0:
        base = 0 - base
    if exp == 0:
        ans = 1
    else:
        ans = base
        inc = base

        for _ in range(1, exp):
            for _ in range(1, base):
                ans += inc
            inc = ans

        if base2 < 0 and exp % 2 == 1:
            ans = 0 - ans

    print(ans)

main()
