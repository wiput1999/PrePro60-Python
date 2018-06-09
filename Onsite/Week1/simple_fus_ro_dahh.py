""" [Simple]Fus ro Dahhh!!!! The series Ep.2 """
def main():
    """ Print result by condition """

    sender = input()
    reciever = input()
    sentence = input()

    size = len(sentence)

    # Message display counter
    counter = 0

    print("%s:Hey, I need you to do something for me." %sender)
    print("%s:I need you to make friends." %sender)
    print("%s:I will take with other races." %reciever)
    print("%s:I will say \"%s\" with them." %(reciever, sentence))
    print("------------")
    if size >= 30 and size <= 60:
        print("* Imperial *")
        counter += 1
    if size >= 50 and size <= 100:
        print("* Argonian *")
        counter += 1
    if size >= 10 and size <= 40:
        print("*  Breton  *")
        counter += 1
    if size >= 0 and size <= 50:
        print("*  Bosmer  *")
        counter += 1
    if size >= 100 and size <= 200:
        print("*  Khajiit *")
        counter += 1
    if size <= 100:
        print("*   Nord   *")
        counter += 1
    if counter >= 3:
        print("* Redguard *")
        counter += 1
    if counter >= 5:
        print("*  Altmer  *")
        counter += 1
    if counter == 0:
        print("* Orisimer *")
        counter += 1
    print("------------")
    if counter <= 1:
        print("%s:I can talk with %d race." %(reciever, counter))
    else:
        print("%s:I can talk with %d races." %(reciever, counter))


main()
