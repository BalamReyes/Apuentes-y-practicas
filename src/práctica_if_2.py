"""
    Ejercicio

    Realizar un programa qpara determinar el costo de un boleto
    a partir de las siguientes condiciones:
    - Costo para una persona menor oo igual a 4 años: Gratis
    - Costo para una persona mayor cuya edad es mayor que 4, 
    pero menor a 18: 200
    - Costo para una persona mayor dd 18: 500

"""
age = input("\n Ingresa tu edad ")
print (age)
#print(type(age))
age = int(age)
#print(type(age))
"""
if age <= 4:
    cost = 0
if age > 4 and age <18:
    cost = 200
if age >= 18:
    cost = 500
print(f"El costo del boleto es {cost}")
"""
        ## Mismo programa, más limpio
# Bloque if-elif-else
print("Programa limpio")

if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0
else:
    cost = 0
print(f"El costo del boleto es {cost}")