#ejercicio 1
#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

n1=int(input("ingrese el numero para generar la tabla de multiplicacion \n"))
print("-----------------")
for i in range(10):
    print(f"{n1} x {i+1} = {n1*(i+1)}")