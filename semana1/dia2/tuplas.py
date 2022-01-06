primos=(2,3,5,7,11,13)
pares=[2,4,6,8,10]
dias=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

primos2=list(primos) #convierte la tupla en lista
primos =tuple(primos2) #convierte la lista en tupla

primosOrdenados = sorted(primos,reverse=True) 
print(primosOrdenados)
print(max(primos)) #obtienes el numero mas alto
print(max(pares))
print(sum(pares)/len(pares))
