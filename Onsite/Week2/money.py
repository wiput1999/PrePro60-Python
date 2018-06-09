""" Money """
def start_money(report):
    """ Calculate start money """
    total = 0
    for data in report:
        if data["type"] == "Receive":
            total += int(data["amount"])
        else:
            total -= int(data["amount"])
    return total

def fn1(rep):
    """ Print function 1 """
    print("money :", start_money(rep))
    print("reportlist")
    for dat in rep:
        print("Type : %s Report : %s Amount : %d" %(dat["type"], dat["detail"], dat["amount"]))

def fn4(rep):
    """ Print function 4 """
    for data in rep:
        if data["type"] == "Receive":
            print("Report : %s Amount : %d" %(data["detail"], data["amount"]))

def main():
    """ Operate by function """

    rep = []

    while True:

        text = input()

        command, argument = text[:3], text[4:]

        if command == "fn1":
            fn1(rep)
        elif command == "fn2":
            argument = argument.split(' ')
            start = start_money(rep)
            rep.append({"type" : "Receive", "amount" : int(argument[0]), "detail" : argument[1]})
            print("%d ==> %d" %(start, start + int(argument[0])))
        elif command == "fn3":
            argument = argument.split(' ')
            start = start_money(rep)
            rep.append({"type" : "disburse", "amount" : int(argument[0]), "detail" : argument[1]})
            print("%d ==> %d" %(start, start - int(argument[0])))
        elif command == "fn4":
            fn4(rep)
        elif command == "fn5":
            for data in rep:
                if data["type"] == "disburse":
                    print("Report : %s Amount : %d" %(data["detail"], data["amount"]))
        elif command == "fn6":
            print("Thank you 3 2 1 ... !@#$%")
            break
        else:
            print("Command_Error.....")
            print("input again!!!")

main()
