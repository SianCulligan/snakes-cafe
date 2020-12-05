# DONE When run, the program should print an intro message and the menu for the restaurant
# DONE The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
# TODO The program should prompt the user for an order
# TODO When a user enters an item, the program should print an acknowledgment of their input
# TODO The program should tell the user how to exit
# DONE The program’s content should match included sample exactly
# DONE Actually, there’s one tiny spot that should be different - see if you can spot it.
# DONE The > character represents user input line and should be printed out with a trailing space.


print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("** ")
print('** To quit at any time, type \"quit\" **')
print("**************************************")

print("Appetizers")
print("----------")
print("Wings")
print("Cookies")
print("Spring Rolls")
print(" ")

print("Entrees")
print("-------")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden")
print(" ")

print("Desserts")
print("--------")
print("Ice Cream")
print("Cake")
print("Pie")
print(" ")

print("Drinks")
print("------")
print("Coffee")
print("Tea")
print("Unicorn Tears")
print(" ")

print("***********************************")
print("***********************************")
print("** What would you like to order? **")
print("***********************************")



# SG create value variable that stores the qty of items ordered
# - have that reflect in the response to user_input (total items ordered ...)

menu_selection = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}



while True:
    user_input = input('> ')
    if user_input == 'quit':
        break
    else:
        menu_selection[user_input] += 1

    for key, value in menu_selection.items():
        if value == 1:
            print ('** 1 order of ' + key + ' have been added to your meal **' )
            user_input
        elif value > 1:
            qty = str(value)
            print ("** " + qty + " orders of " + key + " have been added to your meal **")
            user_input
        else:
            continue











# user_input = input('Anything else? >')

# total qty
# item quantity
# if statement for verbiage

# can use a for loop for full order (see: https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/ )
# user_order
# user input
# wing_order = menu_selection[user_input]
# 
# print(Wings[0])
# print('** '+ ' 1 order of ' + user_input + ' have been added to your meal **' )
# How can we alter the order? 
# menu_selection["Wings"] += 1
# # reads back order
# print(wing_order)
