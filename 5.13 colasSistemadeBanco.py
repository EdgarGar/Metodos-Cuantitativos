'''
Lucia | Adrian | Edgar | Fermin
15.01.2018
Programmed in Python 3 
Used libraries:
random 
math 
-------------------------------------------------------
Colas de banco 

'''
import random
import math

dias = 5 #Numero de dias que correra la simulacion
segundos = 86400 #Segundos en un dia
clientes = 40 #Clientes en 1 hora
ocupado1 = ocupado2= ocupado3 = 0
tiempofila1 = tiempofila2 = tiempofila3 = 0
clientesformados = clientesatendidos =  clienteensistema = 0
tiempoensistema = 0

for hora in range (dias):
    for i in range(segundos): 
        if(i % 90 == 0): #LLegada de los clientes
            clientesformados += 1

        if(clientesformados > 0 and ocupado1 == 0):
            clientesatendidos += 1
            clientesformados -= 1
            ocupado1 = 1
            t = random.randint(0, 60) #Segundos que tardara el cliente
            tiempofila1 = i + t
            tiempoensistema += t
        elif(clientesformados > 0 and ocupado2 == 0):
            clientesatendidos += 1
            clientesformados -= 1
            ocupado2 = 1
            t = random.randint(0, 60) #Segundos que tardara el cliente
            tiempofila2 = i + t
            tiempoensistema += t
        elif(clientesformados > 0 and ocupado3 == 0):
            clientesatendidos += 1
            clientesformados -= 1
            ocupado3 = 1
            t = random.randint(0, 60) #Segundos que tardara el cliente
            tiempofila3 = i + t
            tiempoensistema += t
            
        if(i >= tiempofila1):
            tiempofila1 = 0
            ocupado1 = 0
        if(i >= tiempofila2):
            tiempofila2 = 0
            ocupado2 = 0
        if(i >= tiempofila3):
            tiempofila3 = 0
            ocupado3 = 0
            
        
        
print "Dias transcurridos: {}".format(dias)
print "Horas transcurridas. {}".format((segundos/3600)*dias);
print "Clientes atendidos: {}".format(clientesatendidos);
print "Horas que los clientes pasaron en el sistema: {}".format(round(float(tiempoensistema)/3600,4));
print "Clientes promedio atendidos al dia: {}".format(float(clientesatendidos)/dias);
print "Horas de clientes en el sistema promedio al dia: {}".format(round(float(float(tiempoensistema)/3600)/dias,4));
