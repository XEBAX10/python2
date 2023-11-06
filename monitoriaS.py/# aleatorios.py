import random

while (True):
    a= random.randint(0,10)
    b= random.randint(0,10)
    c= random.randint(0,10)
    d= random.randint(0,10)
    e= random.randint(0,10)
    print(f"indique el resultado de la suma: {a} + {b} + {c} + {d} + {e}")
    respueta=int(input("La respuesta es: "))

    if respueta == a+b+c+d+e:
        print("FELICIDADES, respuesta correcta :)")
        break
    else:
        print("INCORRECTO")
    print("la respues correta es ", (a+b+c+d+e))
    










