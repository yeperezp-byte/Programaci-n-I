# 1. Crear diccionario con información personal
persona = {
    "nombre": "Yeferson",
    "edad": 18,
    "ciudad": "Río Bravo Suchitepequez",
    "lenguaje_favorito": "Python"
}

# 2. Agregar nueva clave 'universidad'
persona["universidad"] = "Universidad de San Pablo"

# 3. Modificar el valor de 'edad'
persona["edad"] = 19

# 4. Iterar con .items() e imprimir cada par
print("Información personal:")
for clave, valor in persona.items():
    print(clave, ":", valor)

# 5. Verificar si 'email' existe con 'in'
if "email" in persona:
    print("El email existe")
else:
    print("yefersonenriqueperezperez@gmail.com")

# 6. Usar .get() para acceder a 'telefono' sin error
telefono = persona.get("telefono", "3594 2608")
print("Teléfono:", telefono)