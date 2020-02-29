#Bryann Eduardo Alfaro
#19372
#Algoritmos y estructuras de datos

#Importar librerias necesarias
import simpy
import random

environment= simpy.Environment()#Crear el espacio del proceso
memoria_RAM= simpy.Container(environment, capacity=100)#Capacidad de 100 para la RAM
CPU_proceso= simpy.Resource(environment, capacity=1) #Solo 1 cpu
random.seed(245) #Haciendo la semilla






