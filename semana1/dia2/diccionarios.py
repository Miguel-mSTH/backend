#son similares a los objetos de javascript
capitales ={'peru':'lima','brazil':'brazilia'}

capital ={'uruguay':'montevideo'}
capitales.update(capital)
c = capitales.pop('bolivia','no existe el pais')

capitales2=capitales.copy()

for capital in capitales:
    print(capital," : ",capitales[capital])

print(capitales.keys())
print(capitales.values())

for clave in capitales.keys():
    print(clave," => ", capitales[clave])

for clave,valor in capitales.items():
    print(clave," -- ", valor)