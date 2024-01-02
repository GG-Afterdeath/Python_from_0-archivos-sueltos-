print("(----------------------------------)")
print("Bienvenido al programa para verificar si el número esss par o impar")
caja= int(input("Por favor, ingrese un número."))

if(caja % 2 == 0):
    print(caja, "es un número par")
elif(caja % 2 ==1):
    print(caja, "es un número impar")
else:
    print("el núemro ingresado no es válido")
