import sys
from heifer_generator import HeiferGenerator
from cow import Cow

def list_cows(cows): # displays available cows from a python list of cow object
    cow_list = [] # creates a list
    for cow in cows: # goes through each list item
       cow_list.append(Cow.get_name(cow)) # adds list item to new list
    return " ".join(cow_list) # joins list items together

def find_cow(name, cows):
    for cow in cows: # iterate through cows and each time look at one cow
        cow_name = Cow.get_name(cow) # sets cow name
        if cow_name == name: # if the name of the cow is equal to name
            return cow # return the cow that is equal
    return None  # return None to indicate we couldn't find the name in cows

if __name__ == "__main__":
    cows = HeiferGenerator.get_cows()
    if sys.argv[1] == "-l": # excludes file name
        print(f"Cows available: {list_cows(cows)}") # call list_cows(cows)
    elif sys.argv[1] == "-n":
        cow = find_cow(sys.argv[2], cows) # Checks for cow match
        message = " ".join(sys.argv[3::]) # stores the message
        if cow:
            print(message) # print the message starting from sys.argv[3]
            print(Cow.get_image(cow)) # print the cow.image
        else:
            print(f"Could not find {sys.argv[2]} cow!")
    else:
        message = " ".join(sys.argv[1::]) # stores the message
        print(message) # prints the message
        print(cows[0].image) # prints the image