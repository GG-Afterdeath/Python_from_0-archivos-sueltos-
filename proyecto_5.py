# String challenges

print("Eliminate one member")

grupo= input("Ingresa el nombre del grupo:  ")
text= input(f"Ingresa los nombres de los miembros de {grupo}:  ")
print(text)
member= input(f"Elimina a un miembro de {grupo}:  ")


print(text.rstrip(member))
