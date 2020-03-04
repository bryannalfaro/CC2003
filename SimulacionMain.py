#Bryann Eduardo Alfaro
#19372
#Algoritmos y estructuras de datos

#Referencias
#https://readthedocs.org/projects/simpy/downloads/pdf/latest/
#https://simpy.readthedocs.io/en/latest/topical_guides/resources.html
#https://docs.python.org/2/library/random.html
#https://docs.sympy.org/latest/index.html
#https://python-para-impacientes.blogspot.com/2016/10/calculo-estadistico.html
#Apoyo de recursos de Canvas sobre el tema de simulaciones

#Importar librerias necesarias
import simpy
import random
import ProcesoPrincipal as procesar

environment= simpy.Environment()#Crear el espacio del proceso
memoria_RAM= simpy.Container(environment, capacity=100)#Capacidad de 100 para la RAM
CPU_proceso= simpy.Resource(environment, capacity=2) #Solo 1 cpu
Espera=simpy.Resource(environment, capacity=1) #La parte donde espera el CPU
random.seed(245) #Haciendo la semilla

cantidad_procesos=25#Cantidad de procesos

for i in range(cantidad_procesos):
    environment.process(
        procesar.ejecucion_procesos(environment,i,CPU_proceso,memoria_RAM,Espera,cantidad_procesos))

environment.run()






