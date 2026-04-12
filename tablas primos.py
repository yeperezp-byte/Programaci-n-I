# =====================================================
# EJERCICIO 5 - TABLAS PRIMOS
# =====================================================

def tabla(n, hasta=10):  # BONUS hasta
    print(f"\nTabla del {n}")
    for i in range(1, hasta+1):
        print(n,"x",i,"=",n*i)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def tablas_primos(limite):
    for n in range(2, limite+1):
        if es_primo(n):
            tabla(n)


# Programa principal
limite = int(input("Hasta qué número: "))
tablas_primos(limite)