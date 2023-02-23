products_qty = input().split()
dict_products_quantities = {}

for k, v in zip(products_qty[0::2], products_qty[1::2]):
    dict_products_quantities[k] = int(v)

searched_product = input().split()
for current_product in searched_product:
    if current_product in dict_products_quantities.keys():
        print(f"We have {dict_products_quantities[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
