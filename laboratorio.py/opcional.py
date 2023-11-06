# calculadora de impuiestos

def calcular_in (impuesto):
    global imp2
    while (True):
        if impuesto < 85528:
            imp2 = (impuesto * 0.18) - 556 + 0.2
            return round(imp2)
        elif impuesto >= 85528 :
             restante = impuesto - 85528
             imp2 = (restante * 0.32) + 14839 + 0.2
             return round(imp2)
        elif impuesto == 0 :
              print("No hay impuesto")
        elif impuesto < 0 :
                    print("Su ingreso no puede ser negativo..")
                    continue

if __name__=='__main__':
    impuesto = float(input("ingresos anuales: "))
    calcular_in (impuesto)
    print(f"su impuesto es {(imp2)}")
