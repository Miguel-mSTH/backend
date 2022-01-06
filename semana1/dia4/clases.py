class Automovil:
    #crear atributos
    def __init__(self,aa,pl,col,mar):
        self.ano=aa
        self.placa=pl
        self.color=col
        self.marca=mar
        self.motor=4000

    def encender(self):
        print('encender ' + self.marca)

    def avanzar(self):
        print('avanzar ' + self.marca)

    def acelerar(self):
        print('acelerar ' + self.marca)

    def frenar(self):
        print('frenar ' + self.marca)

#crear objetos
vw=Automovil(1970,'CH-1234','Amarillo','Volkswagen')
tico=Automovil(1985,'EJ-2345','Rojo','TICO')
lamborghini=Automovil(2018,'E7P-367','Amarillo','Lamborghini')

#utilizar objetos
vw.encender()
print("la placa es : "+vw.placa)
vw.acelerar()
vw.frenar()

tico.encender()
tico.acelerar()
tico.frenar()

lamborghini.encender()
lamborghini.acelerar()
lamborghini.frenar()

vw.color='NEGRO'
#ahora el color es negro
#del vw.color
print("el motor del automovil "+vw.marca+" es de "+str(vw.motor))