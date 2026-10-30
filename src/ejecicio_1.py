"""
sum = 0.0
message =
Sistema de suma de números
Ingresa el valo:
while True:
    value_text = input(message)
    if value_text == 'quit' or \
        value_text == 'q':
        break
    try:
        value = float(value_text)
        sum += value
    except ValueError:
        print("Ingresar un dato válido")
print(f"La suma de los números es {sum}")
"""

total= 0.0
couter = 0
max = None
min = None
while True:
    value_text = input("Ingresa un valor o 'q' 'quit' 'exit'")
    if value_text in ['q', 'quit', 'exit']:
        break
    try:
        value = float(value_text)
    except ValueError:
        print("Dato introducido no válido")
        continue
    total += value
    conter += 1
    if min is None or value < max:
        min = value
    if max is None or value > max:
