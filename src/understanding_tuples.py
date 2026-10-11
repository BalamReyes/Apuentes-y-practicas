"""
                            TUPLAS

    Las tuplas son elementos que no cambian de tamaño.
    Son listas inmutables.


    Se usan los paréntesis () para definir una tupla

    Ejemplo:
        Si tenemos un rectángulo (largo, ancho) que siempre va
        a tener cierto tamaño, podemos asegurar que sus dimensiones
        no van a cambiar si colocamos valores en una tupla
"""

dimensions = (200,50) #200 largo y 50 ancho
print("Tupla original", dimensions)

#Vamos a imprimir una tupla
#De la misma forma que con una lista
print(dimensions[0])
print(dimensions[1])
print(dir(dimensions))

##EJEMPLOS
#Lista
#dimensions_2 = [200,50]
#print(dir(dimensions_2))

#Vamos a modificar el valor de una lista
names = ["Carlos", "Charly", "Juan", "Wendy"]
print(names)
names[0] = "Mercury"
names[1] = "Mercury"
names[2] = "Mercury"
print(names)

#LOOPING
for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla
    lo que si podemos hacer es cambiar
    la asignación de la variable
    que almacena una tupla
"""

dimensions = (500, 1000, 200)
print("Tupla Re-Definida:", dimensions)

        #Tipos de Datos Boleanos
answer = True
print(answer)
#print(dir(answer))