# Sort and Deduplicate a list

def prepare_list(animals):
    # SET for unique items and SORTED to sort alphabetically the items
    final_list = sorted(set(animals))
    # return final_list

# Random list to sort and deduplicate
animals = ['Owl', 'Pig', 'Eagle', 'Pig', 'Tiger', 'Lion', 'Eagle']

# Call the function and start the action
results = prepare_list(animals)
print(results)