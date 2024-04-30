#Librerias implementadas
import numpy as np
import random

#Declaracion de variables
caldo: list;
pos = list;
bol: bool;
opcion: int;


#Funcion para imprimir el tablero.
def ImprimirCultivo(cuadro):
    for i in range(0, len(cuadro)):
        show = print(cuadro[i]);
    return show;


#Funcion para validar el dato suministrado por el usuario.
def ValidarDato(valor, bol):
    bol: bool;
    bol = False;
    if (valor < 10) | (valor > 25):
        bol = False;
    else:
        bol = True;
    return bol;

#Procedimiento para distribuir de forma aleatoria por el tablero el numero de celulas ingresadas por el usuario.
def DistribuirCelulas(tablero, dato):
    for i in range(0, dato + 1, 1):
        tablero[random.randint(0,9)][random.randint(0,9)] = 1;
        dato += 1;

def main():

    print("-----------------------------------")
    print("UCAB, hecho por Freddy Fernandez.")
    print("-----------------------------------")

    bol = False;
    caldo =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ];
    
    while( bol == False):

        data = int(input("Ingresar el numero de celulas vivas en el caldo entre 10 y 25: "));
        
        if (ValidarDato(data, bol) == False):
            print(f"ERROR, el numero suministrado es {data}, y es invalido.");
            print("Por favor ingresar un valor entero entre 10 y 25.");
        else:
            bol = True;
            copy = data;

            DistribuirCelulas(caldo, copy);
            ImprimirCultivo(caldo);

            print (pos)

main();