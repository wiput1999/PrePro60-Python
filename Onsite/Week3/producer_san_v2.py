""" Producer-san_V.1 """
def calculate():
    """ Calculate and display score """
    text = input()
    name, age, smile_ans = text.split('/')
    age = int(age)

    score = 0

    # Add score by counting name len Max : 10 pt
    score += min(10, (len(name) * 1.5))

    if age < 30:
        score += min(10, (30 - age) * 0.5)

    if smile_ans == "Egao":
        score += 10
    elif smile_ans == "Yes":
        score += 5
    elif smile_ans == "No":
        score += 0
    else:
        score -= len(smile_ans) * 0.5

    print("%s / %.1f / " %(name, max(score, 0)), end='')

    if score >= 15:
        print("Pass Project Cinderella")
    else:
        print("Not Pass")

def main():
    """ Calculate and display over condition """

    num = int(input())

    for _ in range(num):
        calculate()

main()
