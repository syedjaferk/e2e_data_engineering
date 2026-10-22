marks = {"tamil": 90, "english": 95}

# print(marks)
# print(marks["tamil"])
# print(marks.get("social", "NA"))
# print(marks["social"])

for key, value in marks.items():
    print(key, value)

orders = [{"product": "lenova v15", "quantity": 2, "unit_price": 10}]
order = orders[0]
print(order["product"], order.get("coupon"), order.get("coupon", "NONE"))
order["amount"] = order["quantity"] * order["unit_price"]  # add a field
print(sorted(order))
print("Total Amount ", order)

print(dict(sorted(order.items())))  # sorted by keys and printing values.
for key, value in sorted(order.items()):
    print(key, value)
# SAME SYNTAX FOR BOTH INSERTION AND UPDATIONS.
