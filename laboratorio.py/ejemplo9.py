"""
Autor: Sebastian Barco
Fecha: 30/10/2023
Descripcion: censo

"""
if __name__ == "__main__":
    print("BIENVENIDO AL CENSO VIRTUAL")
    print("=======================JEFE DEL HOGAR==================\n")
    while(True):
      try:
        nom=str(input("Ingrese su nombre: "))
        apell=str(input("Ingrese su apellido: "))
        Tdoc=str(input("Ingrese su tipo de documento: "))
        Ndoc=str(input("Ingrese su numero de documento: "))
        fecha=str(input("ingrese su fecha de nacimiento  dia/mes/año: "))
        departN=str(input("ingrese su departamento de nacimiento: "))
        ciudadN=str(input("ingrese su ciudad de residencia: "))
        direccionR=str(input("ingrese su direcion de residencia: "))
        cant=int(input("Cantidad de familiares a registrar: "))
        break
      except ValueError:
        print("debes ingresar los datos requeridos correctamente....")

nombre1=[None]*cant
apell1=[None]*cant    
tipo1=[None]*cant  
num1=[None]*cant
fecha1=[None]*cant  
parentesco1=[None]*cant    

def censo():
  n = 0
  while(n < cant):
     print(f"============FAMILIAR {n+1}========================")
     nombre1[n] = input("Ingrese su nombre: ")
     apell1[n] = input("Ingrese su apellido: ")
     tipo1[n] = input("Ingrese su tipo de documento: ")
     num1[n] = input("Ingrese su numero de doc: ")
     fecha1[n] = input("Ingrese su fecha de nacimiento: ")
     parentesco1[n] = input(f"parentes con {nom}: ")
     n = n + 1

  print(f"================================FAMILIA {apell}=====================================")  
  print("==================JEFE DEL HOGAR ================")
  print(f"Nombre   :  {nom} " f"\nApellido  : {apell} " )
  print(f"Tipo de documento   :  {Tdoc} " f"\nNumero de documento : {Ndoc} " )
  print(f"Fecha de nacimiento  :  {fecha} " f"\nDepartamento de nacimiento : {departN} " )
  print(f"Ciudad  :  {ciudadN} " f"\nDireccion  : {direccionR} " )
  print(f"Cantidad de familiares del hogar :  {cant}")
 
  for i in range (0,cant):
   print(f"====================== FAMILIAR{i+1}=====================")
   print(f"Nombre: {nombre1[i]}" f"\nApellido: {apell1[i]}")
   print(f"Tipo de documento: {tipo1[i]}" f"\nNumero de documento: {num1[i]}")
   print(f"Fecha de nacimiento: {fecha1[i]}" f"\nParentesco con {nom}:  {parentesco1[i]}")

censo()
