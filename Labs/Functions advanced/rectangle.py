def rectangle(lenght, width):
    if type(lenght) != int or type(width) != int:
        return "Enter valid values!"

    def area():
        return lenght * width

    def perimeter():
        return (lenght + width) * 2

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))
print(rectangle('2', 10))