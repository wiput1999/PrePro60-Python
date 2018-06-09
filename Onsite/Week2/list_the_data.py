""" List the data """
def main():
    """ List the data into categories """

    result = {"name" : "", "surname": "", "nickname": "", "age": ""}

    for _ in range(10):
        name, surname, nickname, age = input().split(' ')
        result["name"] += (name + " ")
        result["surname"] += (surname + " ")
        result["nickname"] += (nickname + " ")
        result["age"] += (age + " ")

    print("list of name: %s" %result["name"])
    print("list of surname: %s" %result["surname"])
    print("list of nickname: %s" %result["nickname"])
    print("list of age: %s" %result["age"])

main()
