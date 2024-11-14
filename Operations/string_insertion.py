# Insert into a string

def add_product_code(product_code, product_id):
    if product_id[4:9] == product_code:
        return product_id
    else:
        first_part = product_id[:3]
        last_part = product_id[3:]
    return (f"{first_part}-{product_code}-{last_part}")

# Get the product code and ID
product_code = input("Product code: ")
product_id = input("Product ID: ")

# Call the function and print the result
results = add_product_code(product_code, product_id)
print("Product list with code and ID:", results)