"""
Las listas nos permiten almacenar información en un lugar
la cantidad que se desee: Ya sean pocos elementos
o millones de elementos

Una lista es una colección de items (Elementos) que tiene 
un orden particular. Se pueden crear listas que incluyan
strings, enteros, floats, los nombres de las personas de 
tu familia, etc, podemos almacenar (Los tipos de datos
permitidos en python) lo que queramos en una lista

Son elememntos mutables: Puede modificarse el tamaño de la lista

Se recomienda nombrar una variable deñ tipo lista en plural

En python, los corchetes [] indican una lista,
sus elementos se separan por comas

    Ejemplo:
"""
bicycles = ['trek','cannondale', 'redline', 'specialized', 'apache']
print(bicycles)

# Cómo podemos acceder a los elementos de una lista
"""
   Las listas son colecciones ordenadas. Se puede acceder
   a un elemento de una lista diciéndole a Python la posición
   o ídice del elemnto deseado.

   Para obtener el valor deseado se debe escribir
   el nombre de la lista, seguido del índice del elemento 
   entre corchetes
"""

print(bicycles[0], bicycles[1])
print (bicycles[0].upper())

#Los índices comienzan en 0, NO en 1
# bicycles = ['trek','cannondale', 'redline', 'specialized', 'apache']
#Ejemplo:
print(bicycles[0]) #cannonadle
print(bicycles[1]) #Specialized

#Accediendo al último elemento de una lista
print(bicycles[-1]) #Apache
print(bicycles[-2]) #Especialized

# Usando valores individuales
message = f"My firts bicycle was a {bicycles[-1].upper()}"
print (message)
