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









