import requests

api_url = "https://pokeapi.co/api/v2/pokemon/150"
#Primera petición
response = requests.get (api_url, timeout=10)
#recisar errores en la petición
response.raise_for_status()
#Código de estado
print(response.status_code)
pokemon = response.json()
#Imprimir el tipo de variable pokemon
print(type(pokemon))
#print(pokemon)

#IMPRIMIR EL ID
print("Id ", pokemon["id"]) 
print("Name: ", pokemon["name"])
print("No recuerdo: ", pokemon["is_default"])
print("Altura del pokimon: ", pokemon["height"]/10)
print("Peso del pokimon: ", pokemon["weight"]/10)

for element in pokemon["types"]:
    print("Pokimon tipo: ", element["type"]["name"])