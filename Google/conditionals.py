def insert_username(username):
    if len(username) < 3:
        print('{} don`t have more 3 characteres, Try Again '.format(username))
    elif len(username) > 15:
        print("{} invalid username must be at most 15 characters long".format(username))
    else:
        print("Your username {} is valid,Continue your jorney".format(username))

insert_username("Lucasdasdsadaseqeqe")