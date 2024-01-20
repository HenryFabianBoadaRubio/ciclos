#ejercicio 5 
#Escriba un programa que entregue todos los divisores del número entero ingresado:

n1 = int(input('Ingrese el número para generar los respectgivos divisores: \n'))
divisores = []
for i in range(1,int(n1**0.5)):
    if n1%i==0:
        divisores.append(i)
for divisor in reversed(divisores):
    divisores.append(n1/divisor)
print(divisores)