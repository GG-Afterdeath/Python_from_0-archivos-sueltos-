#En las condicionales múltiples la palabra clave es ELIF:

print("=============================================")

print("Adivina el grupo...")
grupo= input("Ingresa las siglas y te diré el grupo")

if(grupo == "BP"):
    print(grupo, "es BlackPink")
elif(grupo == "RDVT"):
    print(grupo, "es Red Velvet")
elif(grupo == "TWC"):
    print(grupo, "es Twice")
elif(grupo == "MMLD"):
    print(grupo, "es Momoland")
else:
    print("Ese grupo es flop, o no existe")
