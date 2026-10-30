"""
Programa que calcule el total de un 
ticket, tomando iva y propina
"""
subtotal_txt = input("Subtotal (MXN): ")
iva_txt = input("IVA (%) Ejemplo 16: ")
tip_txt = input("Propina (%) Ej: 10: ")
try:
    subtotal = float(subtotal_txt)
    iva = float(iva_txt)/100
    tip = float