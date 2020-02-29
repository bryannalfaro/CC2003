#Bryann Eduardo Alfaro
#19372
#Algoritmos y estructuras de datos

import random
#Variables para tiempos y mediciones
tiempo_total=0
tiempo_procesos=[]
tiempo_inicio=0
tiempo_final=0
CPU_instrucciones=3 #Cantidad posible de instrucciones del CPU

#Donde hace el proceso
def ejecucion_procesos(env,nombre,CPU,RAM,Espera):
    intervalo=10 #Intervalo de llegada al CPU
    tiempo_llegada=random.expovariate(1.0/intervalo) #Tiempo de llegada
    cantidad_instrucciones_proceso=random.randint(1,10)#Cuantas instrucciones tiene el proceso
    cantidad_ram_consumida=random.randint(1,10)#Cuanta RAM se va a tomar
    
    yield env.timeout(tiempo_llegada)
    tiempo_inicio=env.now#Tomar el tiempo inicial del proceso para calculos
    
    print("Llego el proceso",nombre,"en momento",tiempo_inicio)
    with RAM.get(cantidad_ram_consumida) as cola1:
        print("Proceso",nombre,"entro a la RAM en",env.now)
        print("Ocupa espacio de: ",cantidad_ram_consumida)
        
        while((cantidad_instrucciones_proceso)>0):
            with CPU.request() as request:
                yield request
                print("Proceso",nombre, "esta corriendo")
                cantidad_instrucciones_proceso=cantidad_instrucciones_proceso-CPU_instrucciones #quitar 3 en este caso
                if((cantidad_instrucciones_proceso)<=0):
                    cantidad_instrucciones_proceso=0 #Eliminar numeros restantes
                    tiempo_final=env.now #Tiempo final del CPU y su proceso
                    RAM.put(cantidad_ram_consumida)#devolver RAM
                    print("Proceso",nombre,"sale del CPU")
                else:
                    eleccion=random.randint(1,2)
                    if(eleccion==1): #Agregar a Waiting
                        with Espera.request() as requestEspera:
                            yield requestEspera
                    else:
                        print("Fue agregado el proceso", nombre, "a ready")
        
    
    