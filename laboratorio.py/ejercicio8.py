
####################################################
print("numeros pares:")
x = 1
while x <= 50:
    if x %2 == 0:
        print(x, end= ' , ')
    x += 1



#############################################################
num=int(input("ingrese un numero: "))
print("\n Los 100 primeros numeors multiplos de ", num)
z = 100
y = 1
a = num
while y <= z:
    if a %a == 0:
        print (a, end= ',')
        y += 1
    a += 1
    
