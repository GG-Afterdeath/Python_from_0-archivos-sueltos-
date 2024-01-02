# strip(elimina los caracteres repetidos del inicio y el final de la cadena)
# También se le puede especificar los caracteres a eliminar,

chain=("Incredibilis  centuria pugna mortis")
print(chain)

chain= chain.strip("Incredi g\pug")
print(chain)
