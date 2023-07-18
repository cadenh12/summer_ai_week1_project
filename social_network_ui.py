# You can implement user interface functions here.
from social_network_classes import Person

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Block/remove friend")
    print("6. <- Go back ")
    return input("Please Choose a number: ")

def editDetails():
    editName = input("Enter your new name:  ")
    editAge = input("Enter your new age:  ")
    editBio =  input("Enter some interesting facts abour yourself:  ")
    return editName, editAge, editBio

def editName():
    print("")
    return input("Enter your new name:  ")

def editAge():
    print("")
    return input("Enter your new age:  ")

def editBio():
    print("")
    return input("Enter some interesting facts abour yourself:  ")


def addFriend():
    print("")
    return input("Plase enter your friend's name:  ") 
#   Person.add_friend(requestedfriend)
#   print("Added friend ...")


#def viewFriends():

#def viewMessages():