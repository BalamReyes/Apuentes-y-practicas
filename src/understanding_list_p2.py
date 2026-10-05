#Agregando elementos a una lista
motorcycles = ['honda', 'mortalika', 'yamaha']
print(motorcycles)

#Método append
motorcycles.append("kawasaki")
print(motorcycles)

"""
EL método append ayuda a crar listas más fácilmente 
de manera dinámica
"""
motorcycles_2 = [] #lista vacía
print(motorcycles_2)
motorcycles_2.append("honda")
motorcycles_2.append("Yamaha")
motorcycles_2.append("Italika")
print(motorcycles_2)

# Metodo .pop() Elimuna el último elemento de la lista, pero nos permite usar el elemento
# después de eliminarlo
print("\n\tAquí aprendí a usar el método pop".upper())
motorcycles_4 = ['honda', 'susukki', 'hd', 'mortalika']
deleted_motorcycle = motorcycles_4.pop() ## [Honda Susuki hd]
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)


#Para eliminar un elemento en específico
motorcycles_5 = ['honda', 'susuki', 'hd', 'mortalika']
print(motorcycles_5)
motorcycles_5.pop(1) ##[susuki, hd, mortalika]
print(motorcycles_5) ##Lista sin susuki
