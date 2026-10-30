                                    #IF STATEMENT

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)

                                    ## EL CONDICIONAL
"""
    El condicional es el corazón de un if.
    Para determinar una igualdad se escribe ==
"""
        #Condicional True/Verdadero
print("\nCondicional True/Verdadero")
truck = "ford"
print(truck =="ford")
print("\nCondicional Verdadero con letra F mayúscula")
print(truck == "Ford".lower()) 
#Se hace verdadero pq a la hora de pasar el texto por .lower, 
#la F se hace minúscula, y se convierte en la variable original
        # Condicional False/Falso
print("\nCondicional False/Falso")
print(truck == "Cheyene")

                             ## Condicional ! para determianr una desiguladad
print("\nCondicional para determianr una desigualdad")
print(truck!="Tacoma") #True
print(truck!="ford") # False

                                ## Conmparaciones numéricas
print("\nComparaciones numéricas")
age = 34
print(age==34) #TRUE
print(age==18) #FALSE
print(age=="34") #FALSO ("34" es un String)

answer = 17
if answer != 42:
    print("Resupesta incorrecta")

age = 19
    # Símbolo menor que
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
age = 21
# Símbolo menor que
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)