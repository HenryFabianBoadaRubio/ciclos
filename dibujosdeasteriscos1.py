#ejercicio 7 
#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

alto= int(input("ingrese la Altura que desea para el rectangulo = \n"))
ancho = int(input("ingrese el ancho que desea = \n "))

for i in range(alto):
    for j in range(ancho):
        print('*', end='')
    print()