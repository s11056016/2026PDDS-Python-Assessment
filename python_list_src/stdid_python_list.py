# Variable Setup
users = [
    { "id": 1, "name": "Alice"},
    { "id": 2, "name": "Bob"}
]

orders = [
    { "id": 1, "user_id": 1, "price": 1000},
    { "id": 2, "user_id": 2, "price": 500 },
    { "id": 3, "user_id": 1, "price": 200 }
]

# Section 1: List joining
'''
Join the users and orders lists based on user_id and id.
Declare a variable "user_orders" to store the result of the join operation.

The result must follow the original order of the orders list (i.e., ordered
by order id: 1, 2, 3). Each record should merge the matching user's name
into the order dictionary.
'''

# Your Code Here
user_orders = []
for order in orders:
    for user in users:
        if user["id"] == order["user_id"]:
            joined = order.copy()          # clone the order dict
            joined["name"] = user["name"]  # merge the user's name into it
            user_orders.append(joined)
            break

print("Section 1: List joining")
print(user_orders)

# Expected Output:
# [{'id': 1, 'name': 'Alice', 'user_id': 1, 'price': 1000}, {'id': 2, 'name': 'Bob', 'user_id': 2, 'price': 500}, {'id': 3, 'name': 'Alice', 'user_id': 1, 'price': 200}]

# Section 2: List Grouping
'''
Group user_orders by name and calculate the total price and order count for
each user. In this dataset each name identifies exactly one user.

1. Declare a dictionary variable "grouped"
2. Use the user's "name" as the key
3. Set the initial value as a dictionary (when the key doesn't exist)
4. Increment the "total_price" and "order_count" for each order

Dict structure:
{
    "name": {
        "total_price": 0,
        "order_count": 0
    }
}
'''

# Your Code Here
grouped = {}
for record in user_orders:
    name = record["name"]
    if name not in grouped:
        grouped[name] = {"total_price": 0, "order_count": 0}
    grouped[name]["total_price"] += record["price"]
    grouped[name]["order_count"] += 1

print("Section 2: List Grouping")
print(grouped)

# Expected Output:
# {'Alice': {'total_price': 1200, 'order_count': 2}, 'Bob': {'total_price': 500, 'order_count': 1}}

# Section 3: List Sorting
'''
Sort the grouped dictionary by "total_price" in descending order
1. Declare a variable "sorted_grouped" to store the result of the sorting operation
2. Use the sorted() function to sort by "total_price" in descending order
'''

# Your Code Here
sorted_grouped = sorted(
    grouped.items(),
    key=lambda item: item[1]["total_price"],
    reverse=True
)

print("Section 3: List Sorting")
print(sorted_grouped)

# Expected Output:
# [('Alice', {'total_price': 1200, 'order_count': 2}), ('Bob', {'total_price': 500, 'order_count': 1})]

# Section 4: List Indexing
'''
Print the details of the user with the highest total price from the sorted_grouped list.
1. Declare a variable "highest_total_price_user" to store the details of the user
   with the highest total price
2. Use indexing to access the first element of the sorted_grouped list and build
   a dictionary with the keys "name", "total_price", and "order_count"
'''

# Your Code Here
top_name, top_stats = sorted_grouped[0]
highest_total_price_user = {
    "name": top_name,
    "total_price": top_stats["total_price"],
    "order_count": top_stats["order_count"]
}

print("Section 4: List Indexing")
print(highest_total_price_user)

# Expected Output:
# {'name': 'Alice', 'total_price': 1200, 'order_count': 2}
