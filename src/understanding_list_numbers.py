#MÉTODO BUILD-IN RANGE

"""
    El método range() nos ayuda a crear fácilmente
    series de números
"""

first_ten_numbers = range(0,10)
for value in first_ten_numbers:
    print(value)
for value in range(1,6):
    print(value)

#Crear una lista usando range
numbers = list(range(0,10))
print(numbers)

#LISTA DE NÚMEROS PARES
even_numbers = list(range(0, 11, 2))
#Que pasa con un paso negativo
print(even_numbers)


five_numbers = list(range(0,50,5))
print(five_numbers)