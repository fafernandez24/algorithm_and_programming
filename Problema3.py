"""Problema 3:
Dado dos números N1 y N2 elabora un Programa en Python que calcule el producto de dichos números
a través del método de sumas recursivas el cual consiste en sumar el Mayor de los dos numeros tantas
veces como lo indica el Menor de los dos números. Se desea mostrar el resultado final y los resultados parciales."""

n1: int;
n2: int;
mayor: int;
menor:int;

def SumaRecursiva(a, b):

    aux: int;
    aux = a;

    for i in range(1, b + 1, 1):
        print(a, end=", ");
        a += aux;

    return print;

def main():

    print("--------------------------------------");
    print("UCAB elaborado por: Freddy Fernandez.");
    print("--------------------------------------");

    n1 = int(input("Ingresar un numero entero: "));
    n2 = int(input("Ingresar otro valor de tipo entero: "));

    if ( n1 >= n2):
        mayor = n1;
        menor = n2;
    
    else:
        mayor = n2;
        menor = n1;

    SumaRecursiva(mayor, menor);

    print("FIN PROGRAMA.")

main();