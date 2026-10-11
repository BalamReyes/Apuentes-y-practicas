players = ["peter", "mercado", "Aaron", "Fátima", "Renata"]
print("Lista Original", players)

    #Slicing
print(players[3:5]) #Fátima Renata (4+1)

"""
    Slicing me permite trabajar con un grupo
    específico  de una lista: Al resultado se le conoce
    como un Slcie
"""

print("1:4", players[1:4])
print(":3", players[:3])
print("2:", players[2:])
print("-3", players[-3:])

    #CASOS ESPECIALES
print("CASOS ESPECIALES")
print(players[1:10])
print(players[-10:10])
print(players[6:1])
print(players[:0])
print(players[0:1])

    #LOOPING
print("lOOPING THOUGHT A SLICE")
students = ["peter", "mercado", "Aaron", "Fátima", "Renata"]

    #Slicing [::] Tarea
for student in students [3:5]:
    print(f"El estudiante {student}, va a pasar la materia")
print(students)

    #CÓMO PODEMOS COPIAR UNA LISTA
my_food = ["Pizza", "Tacos", "Flautas"]
friend_food = my_food #ASI NO SE COPIA UNA LISTA

    #TRES MANERAS CORRECTAS
#Slicing
my_friend_food = my_food[:]
#Método de las listas .copy()
my_friend_food_2 = my_food.copy
#Usar build-in list ()
my_friend_food_3 = list(my_food)