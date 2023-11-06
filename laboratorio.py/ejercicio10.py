def tipo(tipotraba):
  global sueldo
  if tipotraba == "EJECUTIVO":
    sueldo = 3_000_000
  elif tipotraba == "ADMINISTRATIVO":
    sueldo = 2_000_000
  elif tipotraba == "AUXILIAR":
    sueldo = 1_500_000
  else:
    print("categoria invalida..")
    return sueldo

def horas(numerohora , sueldo):
  global horasx
  global suma
  global horast
  if numerohora == 192:
    print("no trabajo horas extras..")
  elif numerohora >= 193:
    horasx = numerohora - 192
    horast = (10416.6666667 * horasx) * 0.2
    suma = sueldo + horast
  elif numerohora < 192:
    print("las horas ingresadas son incorrectas...")
    return  suma

def años (añost, suma, sueldo):
  global salioT
  if añost > 5 :
    salioT = round((suma * 0.2) + sueldo , 2)
  else:
    print("la bonificacion se resive a partir de 5 años..")
    return salioT


if __name__=='__main__':
  while(True):
    try:
      nom = str(input("ingrese el nombre del empeado:"))
      tipotraba= str(input("ingrese su categoria: "))
      numerohora= int(input("ingrese horas trabajadas: "))
      añost= int(input("ingrese años laborados: "))
      break
    except:
      print("Datos invalidos..." "\n vuelve a intentarlo ;)")


  tipo(tipotraba)
  horas(numerohora , sueldo)
  años (añost, suma, sueldo)
  
  
  
  print(f"Nombre: {nom}")
  print(f"Cargo: {tipotraba}")
  print(f"salario base: {sueldo}")
  print(f"salario mas horas extras ({horasx} en total): " f"\n{sueldo} + ({horasx}, horas extra) = {suma}")
  print (f"salario total con bonificacion:" f"\n{sueldo} * 0.2")
  print (f"salario total: {salioT}")


  
