#Bryann Eduardo Alfaro
#19372
#Algoritmos y estructuras de datos

import random
import statistics as stats
#Variables para tiempos y mediciones
tiempo_total_proceso=0
tiempo_procesos=[]
tiempo_final=0
tiempo_inicio=0


CPU_instrucciones=3 #Cantidad posible de instrucciones del CPU


def ejecucion_procesos(env,nombre,CPU,RAM,Espera,procesos):
    
    intervalo=10 #Intervalo de llegada al CPU
    tiempo_llegada=random.expovariate(1.0/intervalo) #Tiempo de llegada
    cantidad_instrucciones_proceso=random.randint(1,10)#Cuantas instrucciones tiene el proceso
    cantidad_ram_consumida=random.randint(1,10)#Cuanta RAM se va a tomar
    
    yield env.timeout(tiempo_llegada)
    tiempo_inicio=env.now#Tomar el tiempo inicial del proceso para calculos
    
    print("Llego proceso",nombre,"en tiempo",tiempo_inicio)
    with RAM.get(cantidad_ram_consumida) as cola1:
        yield env.timeout(tiempo_llegada)
        
        print("Proceso",nombre,"entro a la RAM en",env.now)
        
        #Esto se ejecuta mientras el procesador aun tenga instrucciones por hacer.
        while((cantidad_instrucciones_proceso)>0):
            
            with CPU.request() as request:
                yield request#Requerir al CPU
                yield env.timeout(1)
                
                print("Proceso",nombre, "esta corriendo")
                
                cantidad_instrucciones_proceso=((cantidad_instrucciones_proceso)-(CPU_instrucciones)) #quitar 3 en este caso
               
               if((cantidad_instrucciones_proceso)<=0):
                    cantidad_instrucciones_proceso=0 #Eliminar numeros restantes
                    
                    RAM.put(cantidad_ram_consumida)#devolver RAM
                    print("Proceso",nombre,"sale del CPU")
                    tiempo_final=env.now #Tiempo final del CPU y su proceso
                          
                else:
                    eleccion=random.randint(1,2)
                    print("Random ",eleccion)
                    if(eleccion==1): #Agregar a Waiting
                        with Espera.request() as requestEspera:
                            yield requestEspera#Cola de Waiting                           
                            print("Se agrego a la cola waiting")
                    else:
                        print("Fue agregado el proceso", nombre, "a ready")
                        
        calcularPromedio_Desviacion(tiempo_inicio,tiempo_final,procesos)

        
def calcularPromedio_Desviacion(tiempo_inicio,tiempo_final,procesos):
    print(tiempo_inicio)
    print(tiempo_final)
    tiempo_total_proceso=tiempo_final-tiempo_inicio
    
    tiempo_procesos.append(tiempo_total_proceso)#Agrega a la lista el tiempo de cada proces
    
    print("Procesos: ",procesos)
    promedio=sum(tiempo_procesos)/len(tiempo_procesos)
    if(len(tiempo_procesos)>1):#Esto porque necesita dos datos para poder calcular la desviacion
        desviacion=stats.stdev(tiempo_procesos)
        print("Desviacion: ",desviacion)
    
    print("Total tiempo de proceso",tiempo_total_proceso)
    print("Promedio: ",promedio)
   


    