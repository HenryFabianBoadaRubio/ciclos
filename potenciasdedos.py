#ejercicio 2 
#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

n1= int(input("ingrese el numero para generar las potencias del mismo \n"))
print("-------------------")
for i in range(n1+1):
    print(f"{2**(i)}", end=" ")