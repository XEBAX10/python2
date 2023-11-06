consumo=int(input("ingrese el valor de su consumo: "))


if (consumo > 300):
    consumo -=300
    costo = 300 * 50
    if (consumo<=200):
        costo += consumo * 100
    elif (consumo>200):
        consumo-=200
        costo += 200 * 100
        if(consumo<=500):
            costo += consumo * 150
        elif (consumo >500):
            consumo -= 500
            costo += 500 * 150
            if (consumo>0):
                costo += consumo * 200
elif (consumo<=300):
    costo = consumo * 50

print(costo)
