"""
    Una list comprehension combina el for loop
    y la creación de nuevos elementos 
    en una sola línea y automáticamente agrega
    cada elemenro a la lista, es decir, sin usar
    el método append
"""
squares = [value**2 for value in range(1,11)]
print(squares)

names = ["Renata", "Sebas", "Peter", "Leo", "balam"]
names_UPV = [name + "@upv.edu.mx" for name in names]
print(names_UPV)
