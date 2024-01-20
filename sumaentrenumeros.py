#ejercicio 3
# Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. 
#Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

n1=int(input("ingrese el primer numero \n"))
n2=int(input("ingrese el segundo numero \n"))
suma=0
for i in range(n1 + 1,n2):
    suma+=i
    print(f"la numeros que se suman dentro de los digitos ingresados es {suma}")