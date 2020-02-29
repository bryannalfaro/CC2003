#Bryann Eduardo Alfaro
#19372
#Algoritmos y estructuras de datos

#Importar librerias necesarias
import simpy
import random
import ProcesoPrincipal as procesar

environment= simpy.RealtimeEnvironment()#Crear el espacio del proceso
memoria_RAM= simpy.Container(environment, capacity=100)#Capacidad de 100 para la RAM
CPU_proceso= simpy.Resource(environment, capacity=1) #Solo 1 cpu
Espera=simpy.Resource(environment, capacity=1) #La parte donde espera el CPU
random.seed(245) #Haciendo la semilla

cantidad_procesos=25#Cantidad de procesos

for i in range(cantidad_procesos):
    environment.process(procesar.ejecucion_procesos(environment,i,CPU_proceso,memoria_RAM,Espera))

environment.run()






