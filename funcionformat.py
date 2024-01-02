#Método .format()

print("El método format acepta parámetros, en este caso vamos a pasar variables")

n=input("Hola, por favor dime tu nombre")
sn=input("Ahora dime tu sobrenombre")
a=int(input("Por último, indícame tu edad"))

print("{}, tu nombre real es {} y tienes {} años".format(sn, n, a))
