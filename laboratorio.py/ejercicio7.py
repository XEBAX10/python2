#pago de empleados
cantidad_empleados=int(input("digite numero de empleados: "))
for i in range(cantidad_empleados):
    documento=input("digite el numero de identidad: ")
    nombre=input("digite su nombre completo: ")
    salario=int(input("digite el salario basico del empelado: "))

    subsidio_trans=  salario*0.20
    bonificacion_servi= salario *0.10
    salud=salario*0.04
    pension=salario*0.04
    retefuente=salario*0.05

    total_pago= salario + subsidio_trans + bonificacion_servi
    tota_descuentos=salud + pension + retefuente
    valor_neto=total_pago - tota_descuentos

    print("################### DATOS DEL EMPLEADO ################")
    print(f"Nombre: {nombre}")
    print(f"documento: {documento}")

    print("################### PAGOS ############################")
    print(f"su salario es {salario}")
    print(f"bonificacion de servicios: {bonificacion_servi}")
    print(f"subsidio transporte: {subsidio_trans}")

    print("################### DESCUENTOS ########################")
    print(f"salud: {salud}")
    print(f"pension: {pension}")
    print(f"retefuente: {retefuente}")
    
    print("################## TOTALES ##############################")
    print(f"Total pagos: {total_pago}")
    print(f"Total descuentos: {tota_descuentos}")
    print(f"Neto a pagar: {valor_neto}")
    
