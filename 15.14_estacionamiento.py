'''
Lucia | Adrian | Edgar | Fermín
08.02.2018
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

horas = 24
minutos = 60 
clientes = 10
coche_perdido = coche_estacionado = estacionado = disponibles = 0
    
for hora in range(horas):
    salidas = []
    llegadas = []
    estacionamiento = 6
    for i in range (clientes):
        minuto_llegada = random.randint(1,60)
        llegadas.append(minuto_llegada)
    llegadas.sort() #Ordenar los coches 
    #print llegadas
    for i in range (clientes):
        tiempo = random.randint(10,30)
        salidas.append(tiempo + llegadas[i])

    for i in range (minutos):
        for coche in range (clientes):
            if(llegadas[coche] == i):
                if(estacionamiento > 0):
                    #print "Coche estacionado"
                    coche_estacionado += 1
                    estacionamiento -= 1
                else:
                    #print "Coche perdido"
                    coche_perdido += 1
            if(salidas[coche] == i):
                #print "Coche salio"
                estacionamiento +=  1

promedio_estacionado = float(coche_estacionado)/(clientes*horas)
promedio_perdido = float(coche_perdido)/(clientes*horas)

print "Estacionamiento: {}".format(estacionamiento)
print "Coches que encontraron estacionamiento: {} de {} ".format(coche_estacionado, clientes)
print "Coches que se fueron por estacionamiento lleno: {} de {} ".format(coche_perdido, clientes)
print "Probabilidad de estacionar un coche en {} horas: {}".format(horas,promedio_estacionado)
print "Probabilidad de perder un coche en {} horas: {}".format(horas,promedio_perdido)
