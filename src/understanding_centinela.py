"""
While - senrinel - Centinela
while True
    print("Hola")
Relaizar un programa que capture el importe
y que acumule todos estos importes
en una variable
"""
sum = 0.0
message = """
    SISTEMA GESTOR DE ACUMULACIÓN DE VALORES
    La creatividad está en tus manos

    En todo moemento, si deseas salir puedes
    tipear q, e, quit, exit

Ingresa un valor : """
while True:
    value_txt = input(message)
    if value_txt == 'quit' or \
        value_txt == 'exit' or \
        value_txt == "e" or \
        value_txt == "q":
        break

    try:
        value = float(value_txt)
        sum += value
    except ValueError:
        print("Ingresar un daro válido")
print(f"Tu total acumulado es de {sum} ")
