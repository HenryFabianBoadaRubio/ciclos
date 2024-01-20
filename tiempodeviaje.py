    #ejercicios 6 
#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

tiempoviaje = int(input("Duracción tramo =\n"))
tiempototal=0
while tiempoviaje!=0:
    tiempototal+=tiempoviaje
    tiempoviaje = int(input("Duracción tramo =\n"))
print(f"Tiempo total de viaje: {tiempototal//60}:{str(tiempototal%60).zfill(2)} horas")