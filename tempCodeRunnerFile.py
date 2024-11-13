# Tuple with inserted item at specified index

def insert_item(my_tuple, new_value, index):
    # Slices tuple to index, inserts item, appends remaining original elements
    return my_tuple[:index] + (new_value,) + my_tuple[index:]

# Required data before calling the function
my_tuple = input("Existing tuple: ")
new_value = input("Add the item: ")
index = int(input("In the position: "))

# Call the function and start the action
results = insert_item(my_tuple, new_value, index)
print(results)