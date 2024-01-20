#ejercicio 8 
#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
#la entrada del programa debe ser un número entero n que indique cuántos términos de la suma se utilizará.

n1 = int(input("n1: \n"))
suma=0
for i in range(n1):
    suma+=(-1)**(i)*(1/(2*i+1))
pi = 4 * suma
print(pi)