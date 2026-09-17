item1_name = "Notebook"
item1_price = float("4.99")
item1_qty = int("2")

item2_name = "Pen Pack"
item2_price = float("7.50")
item2_qty = int("1")

item3_name = "Backpack"
item3_price = float("34.99")
item3_qty = int("1")

tax_rate = float("0.075")   # 7.5% sales tax

# Creating the store receipt - top part
print("=" * 12)
print("Store receipt")
print(f'{item1_name} ${item1_price} "x" {item1_qty} ${item1_price * item1_qty}')
print(f'{item2_name} ${item2_price} "x" {item2_qty} ${item2_price * item2_qty}')
print(f'{item3_name} ${item3_price} "x" {item3_qty} ${item3_price * item3_qty}')
print("_" * 12)

# Calculating totals
list_of_totals = [item1_price , item2_price , item3_price]
sum_of_totals = sum(list_of_totals)

# Calculating Taxes
taxes = sum_of_totals * tax_rate

# Printing subtotal
print(f'Subtotal: ${sum_of_totals - taxes:.2f}')
# Printing Tax - Bottom part
print(f'Tax: ${taxes:.2f}')
# Printing Total
print("=" * 12)
print(f'Total: ${sum_of_totals + taxes:.2f}')
print("=" * 12)
