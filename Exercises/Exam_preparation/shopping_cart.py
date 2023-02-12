def shopping_cart(*args):
    cart = {'Soup': [], 'Pizza': [], 'Dessert': []}
    limit_of_products = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    adding_condition = False

    for item in args:
        if item == 'Stop':
            break

        type_of_meal, product = item

        if type_of_meal in cart and product not in cart[type_of_meal]:
            if len(cart[type_of_meal]) < limit_of_products[type_of_meal]:
                adding_condition = True
                cart[type_of_meal].append(product)

    if adding_condition:
        output = ''
        sorted_meals = sorted(cart, key=lambda x: (-len(cart[x]), x))
        for key in sorted_meals:
            output += f"{key}:\n"
            for element in sorted(cart[key]):
                output += f" - {element}\n"

        return output

    return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
