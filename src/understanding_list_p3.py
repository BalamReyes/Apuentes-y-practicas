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
