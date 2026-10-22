# def square(num):
#     return num * num


# numbers = [2, 3, 4, 5, 6, 90, 12]

# sqr_number = []
# for number in numbers:
#     value = square(number)
#     sqr_number.append(value)
# print("SQR numbers ", sqr_number)

# sqr_number = [square(number) for number in numbers if number % 2 == 0]
# print("SQR numbers ", sqr_number)


HEADER = "order_id,order_date,customer_id,city,product,category,quantity,unit_price,status".split(
    ","
)


def parse_order(line):
    r = dict(zip(HEADER, line.strip().split(",")))
    r["order_id"], r["quantity"], r["unit_price"] = (
        int(r["order_id"]),
        int(r["quantity"]),
        float(r["unit_price"]),
    )
    return r


with open("data/orders.csv") as f:
    next(f)
    orders = [parse_order(line) for line in f]
# print(orders)
# print(len(orders))


amounts = []
for order in orders:
    if order["status"] == "delivered":
        amount = order["quantity"] * order["unit_price"]
        amounts.append(amount)
print(amounts)

amounts = [
    o["quantity"] * o["unit_price"] for o in orders if o["status"] == "delivered"
]
print(amounts)
print(sum(amounts))

labels = ["big" if o["unit_price"] >= 10000 else "small" for o in orders[:4]]
print(labels)


for itr 