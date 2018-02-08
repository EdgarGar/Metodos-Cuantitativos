'''
Lucia Garza A01362135
15.01.2018
Programmed in Python 3 
Used libraries:
random 
math 
-------------------------------------------------------
Una tineda tiene un lote de estacionamiento con 6 lugares disponibles. 
Los clientes llegan en forma aleaotoria de acuerdo a un proceso poisson a una razon media
de 10 clientes por hora, y se van inmediatamente si no existen lugares disponibles
El tiempo que un auto permanece en el estacionamiento sigue una distribucion uniforme entre 10 y 30 minutos. 

'''

import random
import math

minutos = 1440 #Simulacion se corre durante 24 horas
clientes = 240 #Clientes por hora
tiempo_total = []
llegadas = []
perdido = coche = salida = estacionado = estacionamiento = 0

for i in range (clientes):
    minuto_llegada = random.randint(1,60)
    llegadas.append(minuto_llegada)
llegadas.sort() #Ordenar los coches 

for i in range (clientes):
    tiempo = random.randint(10,30)
    tiempo_total.append(tiempo + llegadas[i])
    
for i in range (minutos):
    for coche in range (clientes):
        if(llegadas[coche] == i):
            if(estacionamiento == 6):
                perdido += 1
            else:
                estacionado += 1
                estacionamiento += 1
        if(tiempo_total[coche] == i):
            estacionamiento -=  1

promedio_estacionado = float(estacionado)/clientes
promedio_perdido = float(perdido)/clientes

print "Probabilidad de perder un coche: {}".format(promedio_perdido)
print "Probabilidad de estacionar un coche: {}".format(promedio_estacionado)
