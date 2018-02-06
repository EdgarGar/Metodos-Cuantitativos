
import random




def simulacionPedido():
    iterations = 260
    for i in range(iterations):
        dailyDemandRand = random.random()
        if(dailyDemandRand <= 0.02):
            #25
            dailyDemand = 25
        elif(dailyDemandRand > 0.02 and dailyDemandRand <=0.06):
            #26
            dailyDemand = 26
        elif(dailyDemandRand > 0.06 and dailyDemandRand <= 0.12):
            #27
            dailyDemand = 27
        elif(dailyDemandRand > 0.12 and dailyDemandRand <= 0.24):
            #28
            dailyDemand = 28
        elif(dailyDemandRand > 0.24 and dailyDemandRand <= 0.44):
            #29
            dailyDemand = 29
        elif(dailyDemandRand > 0.44 and dailyDemandRand <= 0.68):
            #30
            dailyDemand = 30
        elif(dailyDemandRand > 0.68 and dailyDemandRand <= 0.83):
            #31
            dailyDemand = 31
        elif(dailyDemandRand > 0.83 and dailyDemandRand <= 0.93):
            #32
            dailyDemand = 32
        elif(dailyDemandRand > 0.93 and dailyDemandRand <= 0.98):
            #33
            dailyDemand = 33
        elif(dailyDemandRand > 0.98 and dailyDemandRand <= 1.00):
            #34
            dailyDemand = 34

        deliveryTimeRand = random.random()


        if(deliveryTimeRand <= 0.20):
            #1
            deliveryTime = 1
        elif(deliveryTimeRand > 0.20 and deliveryTimeRand <=0.50):
            #2
            deliveryTime = 2
        elif(deliveryTimeRand > 0.50 and deliveryTimeRand <= 0.75):
            #3
            deliveryTime = 3
        elif(deliveryTimeRand > 0.75 and deliveryTimeRand <= 1.00):
            #4
            deliveryTime = 4

        clientWaitingTimeRand = random.random()

        if(clientWaitingTimeRand <= 0.40):
            #0
            clientWaitingTime = 0
        elif(clientWaitingTimeRand > 0.40 and clientWaitingTimeRand <=0.60):
            #1
            clientWaitingTime = 1
        elif(clientWaitingTimeRand > 0.60 and clientWaitingTimeRand <= 0.75):
            #2
            clientWaitingTime = 2
        elif(clientWaitingTimeRand > 0.75 and clientWaitingTimeRand <= 0.90):
            #3
            clientWaitingTime = 3
        elif(clientWaitingTimeRand > 0.90 and clientWaitingTimeRand <= 1.00):
            #4
            clientWaitingTime = 4

        




if __name__ == '__main__':
    print("Tarea 1 ejercicio 5.11")
    simulacionPedido()
