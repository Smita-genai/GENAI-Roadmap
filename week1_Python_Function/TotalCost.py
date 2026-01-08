## Total cost of items in the shopping cart

def total_cost_items(cart):  # Define a function that calculates total cost from cart items
    total_cost = 0  # Initialize total cost variable to zero
    for item in cart:  # Loop through each item in the shopping cart
        total_cost += item["price"] * item["quantity"]  # Add the product of price and quantity to total cost
    
    return total_cost  # Return the calculated total cost


## Cart data
shopping_cart = [{"name" :"Apple", "price":10, "quantity": 5},  # First item: 5 apples at 10 each
                 {"name": "Oranges", "price": 20, "quantity":10},  # Second item: 10 oranges at 20 each
                 {"name": "Oranges", "price": 20, "quantity":8}]  # Third item: 8 oranges at 20 each

## Calling function
print(total_cost_items(shopping_cart))  # Call function and print the total cost of all items in cart