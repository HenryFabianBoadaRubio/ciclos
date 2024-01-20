#ejercicio 11
# La secuencia de Collatz de un número entero se construye de la siguiente forma:

# si el número es par, se lo divide por dos;
# si es impar, se le multiplica tres y se le suma uno;
# la sucesión termina al llegar a uno.
# La conjetura de Collatz afirma que, al partir desde cualquier número, la secuencia siempre llegará a 
# 1. A pesar de ser una afirmación a simple vista muy simple, no se ha podido demostrar si es cierta o no.
# Usando computadores, se ha verificado que la sucesión efectivamente llega a 1 partiendo desde cualquier número natural menor que 258
# Desarrolle un programa que entregue la secuencia de Collatz de un número entero:


n1= int(input("ingrese el valor de n: \n"))
while n1!=1:
    print(int(n1), end=' ')
    if n1%2==0:
        n1 /= 2
    else:
        n1 = n1*3+1
print(1)