
def promedio():
    parcial1 = float(input("Tarea 1: "))
    tarea1 = float(input("Parcial 1: "))
    tarea2 = float(input("Tarea 2: "))
    eFinal = float(input("Examen final: "))
    participacion = float(input("Participacion: "))

    return round(((parcial1*0.2) + ((tarea1 + tarea2)*0.2)/2 + (participacion*0.2) + (eFinal*0.4)),1)

def promedionota (nota, materia):
    
    if materia=="Fundamentos":
        if nota <2.0:
            return "Malo"
        elif nota >= 2.0 and nota <=3.0:
            return "Deficiente"
        elif nota >=3.0 and nota <=3.8:
            return "Regular"
        elif nota>=3.8 and nota <=4.5:
            return "Bueno"
        elif nota>=4.5 and nota <=5.0:
            return "Exelente"
        else:
            return "Nota invalida"
    elif materia=="CalculoI":
        if nota <2.0:
            return "Malo"
        elif nota>=2.0 and nota <=3.0:
            return"Deficiente"
        elif nota>=3.0 and nota <=3.5:
            return "Regular"
        elif nota>=3.5 and nota<=4.5:
            return"Bueno"
        elif nota>=4.5 and nota <=5.0:
            return "Exelente"
        else:
            return "Nota invalida"
    elif materia=="InglesI":
        if nota<3.0:
            return"Deficiente"
        elif nota >=3.0 and nota <=4.0:
            return"Regular"
        elif nota >=4.0 and nota <=4.5:
            return"Bueno"
        elif nota>=4.5 and nota <=5.0:
            return"Exelente"
        else:
            return"Nota invalida"
    elif materia=="Deporte":
        if nota<=3.0:
            return"Malo"
        elif nota >=3.0 and nota <=4.0:
            return"Regular"
        elif nota>=4.0 and nota <=5.0:
            return"Bueno"
    else:
        return"materia no existente"


if __name__ == "__main__":

    nombre = input("Ingrese su nombre: ")
    materia = input("Ingrese materia:")
    
    promedio = promedio()
    print(promedio)
    
    notafinal = promedionota(promedio, materia)
    print(notafinal)

    print("Nombre del alumno: ", nombre, "\nMateria: ", materia, "\nClasificacion", notafinal)