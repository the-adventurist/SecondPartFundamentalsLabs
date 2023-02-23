product_qty = input()
total_products = 0
total_quantities = 0
dict_products_quantities = {}

while product_qty != 'statistics':
    this_product, its_quantity = product_qty.split(': ')
    its_quantity = int(its_quantity)
    if this_product not in dict_products_quantities:
        dict_products_quantities[this_product] = 0
    dict_products_quantities[this_product] += its_quantity
    product_qty = input()

for this_product in dict_products_quantities.keys():
    total_products += 1
    total_quantities += dict_products_quantities[this_product]

print('Products in stock:')
for this_product in dict_products_quantities.keys():
    print(f'- {this_product}: {dict_products_quantities[this_product]}')
print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantities}')
