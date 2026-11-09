# Isabella Martinez — ISM2411 Lab 11
# Reflection 1: I would use .get() for optional information, like an email,
# so I can show a helpful default. I would use brackets for required fields,
# like a transaction amount, so a missing key stands out.
# Reflection 2: Grouping sales by region reminds me of an Excel PivotTable.
# With Python, I can rerun the same steps on a new batch of data without
# rebuilding the summary by hand.
# AI assistance: ChatGPT helped draft and test the code and draft the reflection.

# Exercise 1
customer = {'name': 'Alice', 'email': 'alice@example.com', 'tier': 'gold', 'ytd_spend': 1200}
print(customer['name'])
print(customer['email'])
print(customer['tier'])
print(customer['ytd_spend'])
print(customer)

# Exercise 2
customer['phone'] = '555-0100'
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['email']
print(customer)

# Exercise 3
print(customer.get('email', 'no email on file'))
try:
    print(customer['email'])
except KeyError:
    print('KeyError: email is missing')

# Exercise 4
for key, value in customer.items():
    print(f'{key}: {value}')
# Without .items(), the loop gives only keys.
for key in customer:
    print(key)

# Exercise 5
tier_discounts = {'bronze': 0, 'silver': 0.05, 'gold': 0.10, 'platinum': 0.15}
tier = customer['tier']
rate = tier_discounts.get(tier, 0)
final_price = 200 * (1 - rate)
print(f'Tier: {tier} | Discount: {rate:.0%} | Final price: $' + f'{final_price:.2f}')

# Exercise 6
customers = [
    customer,
    {'name': 'Jordan', 'email': 'jordan@example.com', 'tier': 'silver', 'ytd_spend': 450},
    {'name': 'Sam', 'email': 'sam@example.com', 'tier': 'gold', 'ytd_spend': 800},
]
for record in customers:
    tier = record['tier']
    discount = 300 * tier_discounts.get(tier, 0)
    print(f"{record['name']} | {tier} | Discount: $" + f"{discount:.2f}")

# Exercise 7
catalog = {
    'Widget A': {'price': 9.99, 'stock': 150},
    'Gadget C': {'price': 49.99, 'stock': 8},
}
for product, details in catalog.items():
    if details['stock'] < 20:
        print(f"LOW STOCK: {product} ({details['stock']} remaining)")

# Exercise 8
transactions = [
    {'region': 'South', 'amount': 300},
    {'region': 'North', 'amount': 150},
    {'region': 'South', 'amount': 200},
]
summary = {}
for transaction in transactions:
    region = transaction['region']
    summary[region] = summary.get(region, 0) + transaction['amount']
for region in sorted(summary):
    print(f'{region}: {summary[region]}')
