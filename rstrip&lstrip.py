# rstrip() elimina los caracteres al final de la cadena (derecha)
# lstrip() elimina los caracteres al inicio de la cadena (izquierda)

text=("El brujo Geralt de Rivia vagaba por el mundo  buscando fortuna")
print(text)

print("Strip")
text= text.strip("a E\l\b\r\u\j\o\a")
print(text)
"""
print("lstrip")
text= text.lstrip("w E\l\b\r\u\j\o")
print(text)

print("rstrip")
text=text.rstrip("w a\n\u\t\r\o\f")
print(text)
"""
