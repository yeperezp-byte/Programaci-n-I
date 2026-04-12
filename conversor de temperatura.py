# =====================================================
# EJERCICIO 3 - CONVERSOR TEMPERATURA
# =====================================================

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

# BONUS Rankine
def fahrenheit_a_rankine(f):
    return f + 459.67

def convertir(valor, origen, destino):

    if origen == destino:
        return valor

    if origen == "F":
        valor = fahrenheit_a_celsius(valor)
        origen = "C"

    if origen == "C":
        if destino == "F":
            return celsius_a_fahrenheit(valor)
        if destino == "K":
            return celsius_a_kelvin(valor)

    if origen == "K":
        valor -= 273.15
        return convertir(valor,"C",destino)

    return None


# Programa principal
v = float(input("Valor: "))
o = input("Origen (C/F/K): ").upper()
d = input("Destino (C/F/K): ").upper()

print("Resultado:", convertir(v,o,d))