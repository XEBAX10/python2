def calcularIMC(altura, peso):
    return round((peso/altura**2), 2)

def clasificacion(imc):

    if imc < 18.5:
        return "Infrapeso"
    elif imc >= 18.5 and imc <= 25:
        return "Normal"
    elif imc >= 25:
        return "Sobrepeso"
    else:
        return "?"

if __name__ == "__main__":

    paciente = input("Nombre paciente: ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    imc = calcularIMC(altura, peso)
    
    print("Nombre: ", paciente, "\nIMC: ", imc, "\nClasificacion: ", clasificacion(imc))


