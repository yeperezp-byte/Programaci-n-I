# =====================================================
# EJERCICIO 7 - MENU RESTAURANTE
# =====================================================

historial = []

def calcular_propina(subtotal, porcentaje):
    return subtotal * porcentaje / 100

def calcular_total(subtotal, propina):
    return subtotal + propina

def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error personas"
    return total / personas

def aplicar_descuento(subtotal, descuento):
    return subtotal - subtotal * descuento / 100

def mostrar_menu():
    print("\n1.Propina")
    print("2.Dividir cuenta")
    print("3.Descuento + propina")
    print("4.Salir")
    print("5.Resumen")

def main():
    while True:

        mostrar_menu()
        op = input("Opción: ")

        if op == "1":
            s = float(input("Subtotal: "))
            p = float(input("Porcentaje: "))
            prop = calcular_propina(s,p)
            total = calcular_total(s,prop)
            print("Total:",total)
            historial.append(total)

        elif op == "2":
            t = float(input("Total: "))
            per = int(input("Personas: "))
            print(dividir_cuenta(t,per))

        elif op == "3":
            s = float(input("Subtotal: "))
            d = float(input("Descuento: "))
            nuevo = aplicar_descuento(s,d)
            p = float(input("Propina: "))
            total = calcular_total(nuevo,calcular_propina(nuevo,p))
            print("Total:",total)
            historial.append(total)

        elif op == "4":
            break

        elif op == "5":
            print("Historial:",historial)

main()