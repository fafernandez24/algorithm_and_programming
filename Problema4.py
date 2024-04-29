"""Problema 4:
Dado un numero N entero positivo comprendido entre (0-10) elaborar un Programa en Python que calcule el Factorial del numero N.
Por definicion el factorial de 0 y 1 es 1 y para numeros mayores se consigue multiplicando todos los numeros desde N hasta 1: Ejemplo 5! = 5 * 4 * 3 * 2 * 1 = 120.

(SOLO RESOLVER CON EL METODO DE SUMAS RECURSIVAS)"""

n: int;
mul: int;
r: int;

def multiplicacion(s):
    mul: int;
    mul = 0;

    for i in range(s, 1, -1):
        mul = mul + i;

    return mul;

def main():

    print("UCAB elaborado por: Freddy Fernandez.");

    n = int(input("Ingresar un numero entero positivo comprendido entre (0-10): "));
    
    if ( n < 0 ) or ( n > 10 ):
        print(f"ERROR, el numero suministrado es {n}");
        print("Debe ingresar un numero entero positivo comprendido entre (0-10).");

    else:

        if ( n == 0 ) or ( n == 1 ):
            print(f"El factorial de {n} es: 1"); 

        if ( n > 1 ) and ( n <= 10 ):

            r = 0;
            caja = 0;

            for i in range(n, 1, -1):
                r = multiplicacion(i) + r;
                print(multiplicacion(i));
            
            print(f"!{n} = {r}");

main()