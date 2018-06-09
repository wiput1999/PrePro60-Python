""" Magic Chef """
def main():
    """ Calculate score by condtion """

    while True:
        text = input()

        score = 0

        for char in text:
            if char == " ":
                score += 100
            elif char in "aeiouAEIOU":
                score -= 75
            else:
                score += 50

        if score <= 150:
            print("cheese")
        elif score >= 151 and score <= 350:
            print("chocolate")
        elif score >= 351 and score <= 600:
            print("banana-milk")
        elif score >= 601 and score <= 800:
            print("pee-po")
        elif score >= 801 and score <= 949:
            print("salmon")
        elif score >= 950 and score <= 1000:
            print("YES! CHEF")
            break
        elif score >= 1000:
            print("rainbow")

main()
