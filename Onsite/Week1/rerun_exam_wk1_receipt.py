""" [Rerun Exam Week 1] - Receipt """
def main():
    """ Print Receipt """
    price = float(input())
    tax = float(input())
    service = float(input())

    print("Gross Total : %.2f baht" %price)
    print("VAT %.2f%% : %.2f baht" %(tax * 100, price * tax))
    inc_service = price * service * (1 + tax)
    print("Service Charge %.2f%% : %.2f baht" %(service * 100, inc_service))
    print("-" * 30)
    print("Total : %.2f baht" %(price + inc_service + price * tax))

main()
