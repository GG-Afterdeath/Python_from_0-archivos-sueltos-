#Condicionales simples

print("(-----------------------------)")

grupo= input("Ingresa el nombre de un grupo: ")
views= int(input("Ingresa la mayor cantidad de vistas de ese grupo: "))

if(views > 1000):
    print(grupo, "es conocido")
else:
    print(grupo, "es flop")

print("(-----------------------------)")
print("Calculemos que tal está el top 3 de tu grupo")

grupo= input("Ingresa el nombre de tu grupo favorito: ")
s_one= float(input("¿Cuantas vistas tiene su canción más famosa? "))
s_two= float(input("¿Cuantas vistas tiene su segunda canción más conocida? "))
s_three= float(input("¿Cuantas vistas tiene su tercera canción más conocida?" ))

average= (s_one + s_two + s_three) / 3
print("Promedio de vistas:", average)

if(average > 50):
    print(grupo, "es conocido")
else:
    print(grupo, "es bastante flop")
