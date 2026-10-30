name = input("¿Cómo te llamas?  ")
age_txt = input("¿Cúal es tu edad?  ")
print(f"Hola {name}, tienes {age_txt} años")
#print("En corea tendrás", age_txt+1) #ERROR
try:
    age = int(age_txt) 
    print(f"Hola {name}, tienes {age} años")
except:
    print("No se admiten letras y/o símbolos")
print("En corea tendrás", age+1)