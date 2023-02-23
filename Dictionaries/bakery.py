products_quantities = input().split()
dict_products_quantities = {}
for x in range(0, len(products_quantities) - 1, 2):
    k = products_quantities[x]
    v = products_quantities[x + 1]
    dict_products_quantities[k] = int(v)
print(dict_products_quantities)
