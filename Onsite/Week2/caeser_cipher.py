""" Cipher the serires :3 - Caeser Cipher (Easy) """
def main():
    """ Decode character """
    alpha = input()

    if alpha in '!@#$%^&*1234567890':
        print(alpha)
    elif alpha in 'abc':
        if alpha == 'a':
            print('x')
        elif alpha == 'b':
            print('y')
        elif alpha == 'c':
            print('z')
    else:
        print(chr(ord(alpha) - 3))

main()
