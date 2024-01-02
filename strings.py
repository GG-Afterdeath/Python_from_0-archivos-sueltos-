"""
La asignación (+=) actualiza el valor almacenado en una variable str
por lo que se le asigne después de esta..
"""
print("-------------------")
print("Actualizar el contenido de cadenas de texto con +=")
mensaje = "Hola"
#La actualización str también hace válidos los espacios
mensaje += " Minne"
print(mensaje)

"""
Concatenación (+): Básicamente, es imprimir dos o más variables que son unidas
en ka impresión
"""

print("-------------------")
print("Concatenación")
message = "G-IDLE es conformado por:"
print(message)
# Sus miembros
spc= " "
m1= "Jeon Soyeon"
m2= "Minnie"
m3= "Shuhua"
m4= "Miyeon"
m5= "Yuqi"

print(message + spc + m1 +spc +m2+ spc + m3+ spc+ m4+ spc +m5 )

print("Concatenar String con Int")

mesiyi= "Los miembros de G-IDLE son:"
x = 5
imp = mesiyi + str(x)

print(imp)

"""
Dentro de una variable que  contenga varios caracteres, se puede
invocar el método find() para recuperar una cadena de texto especifica

El método recorre posición por posición hasta encontrar una coincidencia con lo
específicado
"""

print("-------------------")

msg=("M Y E S")
fnd=(msg.find("Y"))
print(fnd)
print("El método retorna la posición en la que encontró el match específicado")

"""
La extracción sirve para recuperar cadenas de  texto dentro de
un rango [0:0]
"""
print("-------------------")
print("Recuperar cadenas de caractéres especificando un rango")
texto= "G-IDLE en mis tiempos tenía una sexta integrante llamada Soojin"
print(texto)
extraer = texto[5:30]
print(extraer)

#Comparar cadenas de texto
print("-------------------")
print("Comparación a (Yuqi) con b (Yuqi)")
a ="Yuqi"
b="Yuqi"
print(a == b)
print("Commparación c(yuQi) con d(yuqi)")
c="yuQi"
d="yuqi"
print(c == d)







