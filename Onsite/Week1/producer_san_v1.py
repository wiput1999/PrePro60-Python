""" Producer-san_V.1 """
def main():
    """ Calculate and display over condition """
    name = input()
    age = int(input())
    smile_ans = input()

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

    print("Name : %s" %name)
    print("Score : %.1f" %max(score, 0))

    if score >= 15:
        print("Pass Project Cinderella")
    else:
        print("Not Pass")

main()
