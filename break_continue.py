#Ejemplo para break
print("While con la sentencia BREAK \n")
contador=0
while contador <10:
                contador += 1
                if contador == 5:
                    break
                else:
                    print("El contador va en:", contador)
print("Finalizado por: Sentencia Break ejecutada")

#Ejemplo para continue
print("==========================")
print("\nWhile con continue.\n", "Continue reinicia el ciclo hasta la evaluación de la condición")
counter = 0
while  counter <=10:
    counter +=1

    if counter == 5:
        continue
    
    print("El valor de contador va en:", counter)
