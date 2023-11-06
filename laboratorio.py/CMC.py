### CMC ###

def gen(genero,peso,estatura, ):
    if genero == 'Masculino':
        cmc = (13.75 * peso) 
        + (5 * estatura) 
        - (6.76 *edad) 
        + 66
        return round(cmc,2)
    elif genero == 'Femenino':
        cmc = (9.56 * peso) 
        + (1.85 * estatura) 
        - (4.68 *edad) 
        - 655
        return round(cmc,2)
    else:
        print("genero invalido")


if __name__ == '__main__':
    genero = str(input("Digite su genero: "))
    peso = float(input("Digite su peso kilos(k): "))
    estatura = int(input("Digite su estatuta (cm): "))
    edad = int(input("Digite su edad: "))
    caloriasF = gen(genero, peso, estatura)
    print("la cantidad minima de calorias es :", caloriasF )


