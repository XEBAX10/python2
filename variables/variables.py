# Convert the money

menu = """ Welcome to the convert the money🪙

1- Pesos Argentinos - Dollars
2- Pesos Colombianos - Dollars
3- Pesos Mexicanos - Dollars

Enter your money here:

"""
country = int(input(menu))

if country == 1:
    value = float(input("Enter the value money:"))
    convert = value / 350
    print("The values in dollars is: {}".format(convert))
elif country == 2:
    value = float(input("Enter the value money:"))
    convert = value / 3940
    print("The values in dollars is: {}".format(convert))
elif country == 3:
    value = float(input("Enter the value money:"))
    convert = value / 17.13
    print("The values in dollars is:{}".format(convert))
else:
    print("The options is not correct.")
