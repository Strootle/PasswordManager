import random


def genPassword():
    #Default variable to store password
    password = ""

    #Possible characters
    u_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_text = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    special_chars = "!_£&/~?"

    #Add to list to randomly choice a category
    _list = [u_text, l_text, nums, special_chars]

    #For a loop of 18, each category is randomly chosen
    #A random character from the chosen category is selected
    #Character is then appended to the password variable and returned
    for i in range (0,18):
        category = random.choice(_list)
        #print(category)
        cat_len = len(category)
        #print(cat_len)
        index = random.randint(0, cat_len-1)
        character = category[index]
        password += character

    return password
