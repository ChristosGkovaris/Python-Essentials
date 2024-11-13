# Add coffee cake, format menu, sort in reverse alphabetical order

def build_menu(cakes):
    # Add a coffee cake item to the dictionary
    cakes[105] = ["Coffee", 2.39]

    # Create a list of formatted strings
    menu_list = [f"{details[0]} cake - $ {details[1]:.2f}" for details in cakes.values()]

    # Sort the list by cake flavor in reverse alphabetical order
    menu_list.sort(reverse=True)

    return menu_list

# Required data before calling the function
# cakes.keys ==> 100, 101, 102, 103, 104, 105
# cakes.values ==> Carrot, Chocolate, Strawberry, Spice, Vanilla
cakes = { 100: ["Carrot", 1.99], 101: ["Chocolate", 1.99], 102: ["Strawberry", 2.19], 103: ["Spice", 2.29], 104: ["Vanilla", 1.79] }

# Call the function and start the action
results = build_menu(cakes)
print(results)




# ========================================================================
# Solution 2

# Creating an empty list
# items[]

# Using for loop to loop throught the cakes and add them to the empty list
# for flavor, price in cakes.values():
#    items.append(f"{flavor} Cake - ${price}")

# Return the once empty list
# return list(reversed(sorted(items)))
# ========================================================================