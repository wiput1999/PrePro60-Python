""" The Exam Graph """
def main():
    """ Print Exam Graph """

    num = int(input())

    result = {}

    for _ in range(num):
        name, score = input().split(' ')
        result[name] = int(score)

    for key in sorted(result.keys()):
        print("%10s: %s" %(key, "*" * (result[key] // 5)))

main()
