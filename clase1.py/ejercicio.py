#convert the money

menu="""welcome to the convert the money 

1- pesos_argentinos - Dollars
2- pesos_comlobianos - Dollars 
3- pesos_mexiconos - Dollars 

enter you money here:

"""
county = int(input(menu))


if country == 1:
    value = float(input("enter the value  money:")) 
    covert = value / 350 


    
elif country == 2:
    value = float(input("enter the value  money: ")) 
    covert = value / 3940 


elif country == 3:
    value = float(input("enter the value  money: ")) 
    covert = value / 17

else:
    print("the options not corret")
  

