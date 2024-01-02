print("========================================")

print("Hola. Bienvenid@ al derecho a vaKciones 1 the K :)")

nombre= input("Ingrese su nombre ")
clave= int(input("Ingrese su clave (1, 2 o 3) "))
años= int(input("Ingrese cuantos años lleva en la empresa :) "))

if(clave == 1):
    if(años == 1):
        print(nombre, "tiene derecho a 6 días de vacaciones")
        print("Terminado")
    elif(años >1 and años <=6):
        print(nombre, "tiene derecho a 14 días de vacaciones")
        print("Terminado")
    elif(años >=7 and años <=50):
        print(nombre, "tiene derecho a 20 días de vacaciones")
        print("Terminado")
    else:
        print(nombre, "no tiene derecho a vacaciones")
        print("Terminado")

elif(clave==2):
    if(años == 1):
        print(nombre, "tiene derecho a 7 días de vacaciones")
        print("Terminado")
    elif(años >1 and años <=6):
        print(nombre, "tiene derecho a 15 días de vacaciones")
        print("Terminado")
    elif(años >=7 and años <=50):
        print(nombre, "tiene derecho a 22 días de vacaciones")
        print("Terminado")
    else:
        print(nombre, "no tiene derecho a vacaciones")
        print("Terminado")

elif(clave==3):
    if(años == 1):
        print(nombre, "tiene derecho a 10 días de vacaciones")
        print("Terminado")
    elif(años >1 and años <=6):
        print(nombre, "tiene derecho a 20 días de vacaciones")
        print("Terminado")
    elif(años >=7 and años <=50):
        print(nombre, "tiene derecho a 30 días de vacaciones")
        print("Terminado")
    else:
        print(nombre, "no tiene derecho a vacaciones")
        print("Terminado")
else:
    print("La clave no existe")
    print("Terminado...")

print("Gracias por usar el programa")






















