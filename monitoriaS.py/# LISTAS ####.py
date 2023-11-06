# LISTAS ####
#lista= vairable de variables "caja donde meten las otras cajas"
# CREAR ##
#append = agregar a la lista
#insert= agregar a lista en la posicion deseasda 
# ELIMINAR ##
# remove = busca el elemnto y lo elimina
# pop= elimina por posicion 



# lista=[0,1,2,3,4,5,6,7,8,9,10]
# tamaño=len(lista)
# for i in range (0, tamaño):
#     print(lista[i])

##### EJEMPLOS ####

# numero = int(input("cuantas matrias tiene?: "))

# lista = []
# for i in range (0, numero):
#     asignaturas= str(input("ingrese el nombre de la materia:"))
#     lista.append(asignaturas)

# print(lista)

#### mejor hecho ## 

# def pedir_datos(lista):
#     materia=str(input("ingrese la materia: "))
#     lista.append(materia)
#     return lista

# if __name__== '__main__':
#     lista=[]
#     for number in range(0,6):
#         pedir_datos(lista)
#     print(lista)


############ EJEMPLO 2 #######

# def pedir_datos(lista):
#     materia=str(input("ingrese la materia: "))
#     lista.append(materia)
#     return lista

# if __name__== '__main__':
#     lista=[]
#     for i in range (0,6):
#         pedir_datos(lista)

#     for i in range(0,6):
#         print("yo estudio", lista[i])



###### EJEMPLO 3 ###########

# def pedir_meterias(lista_1):
#     materia=int(input("ingrese la materia: "))
#     lista_1.apppend(materia)
#     return lista_1
# def pedir_notas(lista_2):
#     nota=int(input("ingrese la nota de la materia: "))
#     lista_2.apppend(nota)


##### INVESTIGACION ############    
#lista=[]#lista vacia, se le pueden agregar, sumar y literanmente utilizar para muchas cosas
#lista = ["lunes", "martes" , "miercoles", "jueves", "viernes" , 30 , 5.96, [3, 5, 6], True]
# tol = len(lista)
# print(tol)
#print(lista[7][1])#buscar una lista dentro de una lista
# lista2 = [1,2,4,5,6,7,8,9,]
# lista2.append(10) #insertar al final de la lista
# print(lista2)

# lista2.insert(2,3)  #insertar en un lugar especifico de la lista (luagr : lo que quiero insertar)
# print(lista2)

# lista2.extend([11,12,13,14,15]) #agregar  a una lista 
# print(lista2)

# lista3 = lista + lista2 #sumar listas 
# print(lista3)
       
#lista = [2, -3, 15, 0, 78, 11] 
#lista.sort(reverse=True) #ordena decendentemente

#lista.sort() #ordena acendentemente

# lista.reverse() #voltea la lista

#lista.clear()  #elimina la lista por completo

#lista.remove(1) #elimina el elemento deseado 

# lista.pop() # busca y elimina el indice deseado
#print(lista)
#print(6 in lista ) #buscar en la lista

# print(lista.index(2)) #en que lugar de la lista esta 
# print(lista.count(3)) #contar cuantas veces esta el elemnto

#lista=[2, 4, 5, 8, 9, 10]
# print(lista[0:6])#imprimir un rango dentro de una lista
# print(lista[0], lista [5])#imprimir elemntos de una lista por separado
# lista2=lista[1:4]#asignar un pedazo de la lista a una variable
# print(lista2)

import random
lista_random=[]
for i in range (10):
    lista_random.append(random.randint(1,16))

lista_random.sort()
print(lista_random)
lista_random.reverse()
print(lista_random)