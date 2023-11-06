#####notas de alumnos####
def calcularDefinitiva(parcial, examen,tarea1, tarea2 ,participacion):
    parcial=20/100* parcial
    examen=40/100* examen
    tareas =20/100*((tarea1+tarea2)/2)
    participacion=20/100* participacion

    return tareas + parcial + participacion + examen

def calcularclasificacion(nota, materia):
    if materia=="Fundamentos":
        if nota < 2.0:
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
        if nota < 3.0:
            return"Deficiente"
        elif nota >=3.0 and nota <=4.0:
            return"Regular"
        elif nota >=4.0 and nota <=4.5:
            return"Bueno"
        elif nota>=4.5 and nota <=5.0:
            return"Exelente"
        else:
            return"Nota invalida"
    elif materia == "Deporte":
        if nota < 3:
            return"Malo"
        elif nota >=3 and nota <=4:
            return"Regular"
        elif nota>=4 and nota <=5:
            return"Bueno"
    else:
        return"La materia no existente"


if __name__ == "__main__":

  
  while(True):
   try:
    
    nombre =str(input("Ingrese su nombre: "))
    materia=str(input("Ingrese la materia: "))
    break
   except: 
    print("Debes introducir tu nombre y la materia deseada ")
while(True):
  try:
    
    parcial=float(input("Ingrese la nota del parcial: "))
    examen=float(input("Ingrese la nota del examen : "))
    tarea1=float(input("Ingrese la nota tarea 1: "))
    tarea2=float(input("Ingrese la nota tarea 2: "))
    participacion=float(input("Ingrese la nota de participacion : "))
    break
  
  except:
      print("INGRESE UN NUMERO VALIDO: (INT), (FLOAT)")
      


  


promedio = calcularDefinitiva(parcial , examen, tarea1, tarea2, participacion )
clasificacion = calcularclasificacion(promedio, materia)

print("nombre del alumno: ", nombre,"\nmatria: ", materia, "\nnota final: ", promedio ,  "\nclasificacion: ", clasificacion)
    

    


