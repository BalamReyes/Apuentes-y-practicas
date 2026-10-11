#Trabajando con listas
print("\n\tHoy vamos a aprender a hacer listas")
magicians = ['harry','ron' ,'hermione', 'snape','voldemort']
print(magicians)
print("imprimir a la mala".upper())
print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4])

#ciclo FOR
print("ciclo for".upper())
for magician in magicians:
    print(magician)
#ciclo FOR
print("ciclo for seguido".upper())
for magician in magicians:
    print(magician, end=" ")
print(" ")
# A esto se le llama lupping
# for cat in cats:
# for dog in dogs:

#Ahora vamos a impromir cun menmsaje para cada mago
for magician in magicians:
        print(f"{magician.title()} ese fue un gran hechizo")
        print(f"no puedo esperar a ver el siguiente hechizo {magician.upper()}\n")
print("Ese fue un gran espectáculo")

#IDENTACIÓN
"""
    Python utiliza la idengtación para determinar
    cuando una línea de código está conectada a la
    líea de código anterior

    Básicamente, se usan 4 espacios en blando para
    obligarnos a escribir código ordenado y estructurad
"""
# No olvidemos identar- Tracenack IdentationError
magicians = ["alice", "david", "caroline"]
#for magiian in magicians:
#pritn(magician) #identation error

#Error de lógica- Logic error- IdentationError
for magician in magicians:
     print(magician)
print(f"No puedo esperar a ver el hechizo, {magician}")

#CORRECTO
for magician in magicians:
     print(magician)
     print(f"no puedo esperar a ver el siguiente hechizo, {magician}")
# Identación innecesaria
#message = "Hello World"
#    print(message)

#ERROR DE SINTAXIS NO OKVIDAR LOS :
#for magician in magicians
#    print(magician)