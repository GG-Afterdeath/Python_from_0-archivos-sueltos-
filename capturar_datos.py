#Capturar datos desde la consola
"""
Capturar:
    String
    Integer
    Float
    Complex
"""
print("(---------------------------------------)")
grupo= input("Introduce el nombre de un grupo: ")
miembros = int(input("Cuantos miembros tiene " + grupo +": "))
altura = float(input("Introduce la altura máxima de algún integrante de "+ grupo+": "))
num_complex= complex(input("Cantidad de pasos por segundo:"))

print("(str) Nombre:", grupo)
print("(int) Miembros:", miembros)
print("(float) Altura máxima en el grupo:", altura)
print("(complex) Cantidad de pasos por segundo:", num_complex)
