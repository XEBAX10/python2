#ejemplo 3#

def total(edad,nombre,meses):
    if edad <12:
        categoria = "Infantil"
        a = 43000
    elif edad >=12 and edad <18:
        categoria = "Juvenil"
        a= 36000
    elif edad >=18:
        categoria ="Mayores"
        a= 32000
    else:
        categoria = "Edad invalida"
    return print(f"Nombre: {nombre} \nCategoria: {categoria}\nTotal a pagar: ",a*meses)
          

if __name__ == "__main__":
    nombre=input("digite su nombre: ")
    ed = int(input("edad:"))
    meses=int(input("cantidad de meses: "))
    total(ed,nombre,meses)
    