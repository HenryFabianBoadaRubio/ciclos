#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

lado1=int(input("ingrese el tamaño que desea para el hexagono = \n"))
final_length = lado1 + 2*(lado1-1)
for i in range(lado1):
    final_string=""
    for j in range(lado1+2*i):
        final_string+="*"
    print(final_string.center(final_length))
for x in range(1,lado1):
    final_string=""
    for j in range(2,lado1+2*(lado1-x),1):
        final_string+="*"
    print(final_string.center(final_length))