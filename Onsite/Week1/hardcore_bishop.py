""" [Hardcore] - Bishop """
def main():
    """ Calculate that bishop can walk to dest or not? """

    start = input().lower()
    dest = input().lower()

    start_x = ord(start[0])
    start_y = int(start[1])
    dest_x = ord(dest[0])
    dest_y = int(dest[1])

    if dest_x - start_x == dest_y - start_y or dest_x - start_x == (dest_y - start_y) * -1:
        print("True")
    elif dest_y - start_y == dest_x - start_x or dest_y - start_y == (dest_x - start_x) * -1:
        print("True")
    else:
        print("False")

main()
