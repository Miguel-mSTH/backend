# f = open('alumnos.txt','w') #w es un write pero lo sobrescribe, (a) no sobreescribe, (a+) lectura y escritura
# f.write('\nCesar Mayta')

f = open('alumnos.txt','r')
alumnos = f.read()
print(alumnos)

lstResultado=[]

lstAlumnos = alumnos.splitlines() #lo convierte en una lista
print(lstAlumnos)

for dictAlumno in lstAlumnos:
    lstdictAlumno = dictAlumno.split(',') #lo convierte en un diccionario
    print(lstdictAlumno)
    dictAlumno={
        'nombre':lstdictAlumno[0],
        'email':lstdictAlumno[1],
        'celular':lstdictAlumno[2]
    }
    lstResultado.append(dictAlumno)
print(lstResultado)
f.close