#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            theuser = ai_social_network.create_account()


        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "6":
                    break
#                   inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == "1":
                    #edittedName, edittedAge, edittedBio = social_network_ui.editDetails()
                    edittedName = input("Enter your new name, your original name was " + str(theuser.id) + "  New name: ")
                    edittedAge = input("Enter your new age, your original name was " + str(theuser.year) + "  New age: ")
                    bio = input("Enter some interesting facts about yourself: ")
                    theuser.id = edittedName
                    theuser.year = edittedAge
                    theuser.bio = bio
                    break
                elif inner_menu_choice == "2":
                    #requestedfriend = str(social_network_ui.addFriend())
                    requestedfriend = input("What is your friends name:  ")
                    #THEUSER || UNBOUND CLASS
                    theuser.add_friend(requestedfriend)
                    break
                elif inner_menu_choice == "3":
                    theuser.viewFriends()
                    break
                elif inner_menu_choice == "4":
                    print(inner_menu_choice)
                elif inner_menu_choice == "5":
                    removefriend = input("Type the name of the user you want to remove from the friends list:  ")
                    if removefriend in theuser.friendlist:
                        theuser.remove_friend(removefriend)
                        print("Friend succesfully removed")
                    else:
                        print("The friend is not in the friendlist.  ")
                    break
                else:
                    print("ERROR")

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
