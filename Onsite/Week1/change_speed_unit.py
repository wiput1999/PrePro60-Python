""" Change speed unit """
def main():
    """ Convert speed unit """
    speed = float(input())

    print("%.4f foot per second." %(speed * 3.2808))
    print("%.4f miles per hour." %(speed * 2.2369))
    print("%.4f kilometer per hour." %(speed * 3.6))

main()
