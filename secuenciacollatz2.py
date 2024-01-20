
#Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros positivos menores que el ingresado por el usuario:

n1 = int(input("ingrese el valor de n =\n "))
j=0
for i in range(1,n1+1):
    j=i
    len=1
    while j!=1:
        len+=1
        if j%2==0:
            j /= 2
        else:
            j = j*3+1
    imprime = len * '*'
    print(f'{i} {imprime}')