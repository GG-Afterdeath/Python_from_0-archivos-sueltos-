print("========================")
print("Bienvenidos a la balanza de números")
uno= int(input("Ingrese un número en el cajón 1"))
dos= int(input("Ingrese un número en el cajón 2"))
tres= int(input("Ingrese un número en el cajón 3"))

if(uno>dos and uno>tres):
    print(uno, "es el número mayor, se encuentra en el primer cajón")
elif(dos>uno and dos>tres):
    print(dos, "es el número mayor, está guardado en el segundo cajón")
elif(tres>uno and tres>dos):
    print(tres, "es el número mayor, está guardado en el tercer cajón")
else:
    print("Los números son iguales")
