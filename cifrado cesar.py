# =====================================================
# EJERCICIO 6 - CIFRADO CESAR
# =====================================================

def cifrar_caracter(c, desplaz):
    if not c.isalpha():
        return c

    base = ord('a') if c.islower() else ord('A')
    nueva_pos = (ord(c) - base + desplaz) % 26
    return chr(base + nueva_pos)

def cifrar_mensaje(mensaje, desplaz):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplaz)
    return resultado

def descifrar_mensaje(mensaje, desplaz):
    return cifrar_mensaje(mensaje, -desplaz)

# BONUS fuerza bruta
def fuerza_bruta(mensaje):
    for i in range(26):
        print(i,":",descifrar_mensaje(mensaje,i))


# Programa principal
msg = input("Mensaje: ")
d = int(input("Desplazamiento: "))

cifrado = cifrar_mensaje(msg,d)
print("Cifrado:", cifrado)
print("Descifrado:", descifrar_mensaje(cifrado,d))

fuerza_bruta(cifrado)