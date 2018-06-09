""" The Noise """
def main():
    """ Print by condition """
    var_a = float(input())
    var_b = float(input())
    if var_a % 2 == 0:
        var_c = float(input())
        if var_c == var_b:
            print('My heart goes Sha la la lal la\nclap clap clap')
        elif var_b >= 0:
            print('My heart will go on and on\nuh hmm ummm')
        elif var_b < 0:
            print('My heart goes Sha la la la Just for you')
    elif var_a % 2 != 0:
        if var_b % 2 == 0:
            print("What's in your head!! In your head!!")
        elif var_b % 2 != 0:
            print("What's in your head!! Zombie Zombie!\nZombie ei ei eh oh!")

main()
