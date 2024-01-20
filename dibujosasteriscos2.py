#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

alto = int(input("ingrese la Altura que desea para el triangulo= \n"))

for i in range(alto):
    for j in range(i+1):
        print("*", end="")
    print()