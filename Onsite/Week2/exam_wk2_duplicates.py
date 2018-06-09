""" Duplicates """
def main():
    """ Find Duplicates or not? """
    num = int(input())

    data = []

    for _ in range(num):
        text = input().lower()
        dup = 0
        for dat in data:
            if text == dat:
                dup = 1
                break
        if dup == 1:
            print("Yes")
        else:
            print("No")
        data.append(text)

main()
