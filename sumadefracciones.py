
#ejercicio 9 
# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:

# 12,14,18,116,132,164,…
# en forma decimal:

# 0.5,0.25,0.125,0.0625,0.03125,0.015625,…
# El programa debe mostrar tres columnas que contengan la siguiente información:

fracciones=1
i = 1
suma=0
titulos = ['Potencia', 'Fracción', 'Suma']
for header in titulos:
    print(header, end=' ')
print()
while fracciones>0.000001:
    fracciones=1/(2**i)
    suma += fracciones
    print(str(i).ljust(8), end=' ')
    print(str(round(fracciones,4)).ljust(8), end=' ')
    print(round(suma,4))
    i+=1


