#realizar un programa que te pida ingresar una cantidad de numeros. el programa debe pedirte cuantos numeros ingressar al final debe mostrar el numero mayor, menor, el promedio y debe mostrar todos los numeros ordenados en una tupla.

valores=[]
n=int(input("ingrese la cantidad de valores a evaluar : "))

for i in range(n):
    valor = int (input("ingrese valor "+str(i+1)+": "))
    valores.append(valor)

maximo = max(valores)
minimo = min(valores)
promedio = sum(valores)/len(valores)
valoresOrdenados=sorted(valores)

print(maximo)