def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_products = []
    budget_left = budget

    for product in grocery_list:
        if product not in purchased_products:
            for el in args:
                if product == el[0]:
                    if budget_left >= el[1]:
                        budget_left -= el[1]
                        purchased_products.append(product)
                        break
                    else:
                        break
        continue

    if len(purchased_products) == len(grocery_list):
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join([item for item in grocery_list if item not in purchased_products])}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
