"""
- Listas de diccionarios
- Listas en diccionarios
- Diccionarios de diccionarios
"""
#Liastas de diccionarios
covenant_elite = {
    "name": "elite",
    "color": "blue",
    "points": 10,
    "shield": True
}
covenant_jackal = {
    "name": "jackal",
    "color": "gray",
    "points": 6,
    "shield": True    
}
covenant_grunts = {
    "name": "grunt",
    "color": "orange",
    "points": 3,
    "shield": False
}
#Nesrund de ka ista de diccionarios
covenants = []
covenants.append(covenant_elite)
covenants.append(covenant_jackal)
covenants.append(covenant_grunts)
print(covenants)

#Flotilla de enemigos
covenants_fleet = []
for _ in range(2):
    covenants_fleet.append(covenant_elite)
for _ in range(5):
    covenants_fleet.append(covenant_jackal)
for _ in range(20):
    covenants_fleet.append(covenant_grunts)
print("Flotilla")
print(covenants_fleet)


#Nesting: Una lista en diccionarios
#Menu
print("\n NEsting: Listas en diccionarios")
tacos = {
    "tortillas" : ["maiz", "harina"],
    "guisos" : ["bistek", "tripa", "pastor"]
}
print

