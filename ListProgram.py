# Program to manipulate a list

# Variable declaration
# running is a boolean variable to control the while loop
running = True
# the list to hold the names
names = ["Joe", "Bob", "Sam"]

# Main loop for the program
while running:  # The loop will run until running is changed to False
    # display the menu
    print()
    print("0. Exit")
    print("1. Display a sorted list of guests.")
    print("2. Add a guest to the list.")
    print("3. Delete a guest from the list.")
    # accept the users input
    menu_option = int(input())
    if menu_option == 0:  # Exit the menu
        running = False  # When the loop checks the condition it will exit
    elif menu_option == 1:  # Display the list
        names.sort()  # Sorts the names list
        for name in names:  # for loop that iterates through the names list
            print(name)  # prints each name in the list
    elif menu_option == 2:  # Add a name
        print("\nEnter a name to add to the list:")
        new_name = input()
        if new_name in names:  # if the new_name is in the names list
            print("\nThat name is already in the list")
        else:
            names.append(new_name)  # appends the new_name to the list
    elif menu_option == 3:  # Delete a name
        print("\nEnter a name to remove from the list")
        del_name = input()
        if del_name not in names:  # if the del_name is not in the names list
            print("\nThat name is not in the list")
        else:
            names.remove(del_name)  # remove the del_name from the names list
    else:
        print("\nThat is an invalid option")  # print this if user enters anything other than 0,1,2,3
        print("Please choose 0, 1, 2, or 3")


