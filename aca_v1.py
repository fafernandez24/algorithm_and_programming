# Librerias implementadas
import random

# Declaracion de variables
caldo: list;
pos = list;
bol: bool;
opcion: int;

# Funcion para imprimir el tablero.
def ImprimirCultivo(cuadro):
    for i in range(0, len(cuadro)):
        show = print(cuadro[i]);
    return show;

# Funcion para validar el dato suministrado por el usuario.
def ValidarDato(valor, bol):
    bol: bool;
    bol = False;
    if (valor < 10) | (valor > 25):
        bol = False;
    else:
        bol = True;
    return bol;

# Procedimiento para distribuir de forma aleatoria por el tablero el numero de celulas ingresadas por el usuario.
def DistribuirCelulas(tablero, dato, pos):
    for i in range(0, dato, 1):
        tablero[random.randint(0,9)][random.randint(0,9)] = 1;
        dato += 1;

# Funcion que permite al usuario agregar una celula en la posicion indicada.
def AgregarCelula(tablero, vertical, horizontal):
    vertical += 1;
    horizontal += 1;

    if (tablero[vertical][horizontal] == 1):
        return print(f"ERROR, la posición {tablero[vertical][horizontal]} ya esta ocupada.");
    else:
        tablero[vertical][horizontal] = 1;
        return tablero[vertical][horizontal];

# Funcion que permite al usuario eliminar una celula en la posicion indicada.
def EliminarCelula(tablero, vertical, horizontal):
    vertical += 1;
    horizontal += 1;

    if (tablero[vertical][horizontal] == 0):
        return print(f"ERROR, la posición {tablero[vertical][horizontal]} ya se encuentra desocupada.");
    else:
        tablero[vertical][horizontal] = 0;
        return tablero[vertical][horizontal];

def MenuOpciones(tablero):

    bol: bool;
    opcion:int;
    fila: int;
    columna: int;

    bol = False;

    print("------------------------");
    print("===== OPCIONES =====");
    print("------------------------");
    print("");
    print("(1) Agregar celula");
    print("(2) Eliminar celula");

    while (bol == False):

        opcion = int(input("Elegir una opcion: "));

        if (opcion == 1):
            fila = int(input("Ingresar fila(1-10): "));
            columna = int(input("Ingresar columna(1-10): "));
            if (fila < 1) | (fila > 10):
                print("---------------------------------------------------------------------------");
                print(f"ERROR, el numero suministrado es {fila}, por lo tanto, es invalido.");
                print("Por favor ingresar un valor entero entre 1 y 10.");
                print("---------------------------------------------------------------------------");
            elif (columna < 1) | (columna > 10):
                print("---------------------------------------------------------------------------");
                print(f"ERROR, el numero suministrado es {columna}, por lo tanto, es invalido.");
                print("Por favor ingresar un valor entero entre 1 y 10.");
                print("---------------------------------------------------------------------------");
            else:
                AgregarCelula(caldo, fila, columna);

        elif (opcion == 2):
            fila = int(input("Ingresar fila(1-10): "));
            columna = int(input("Ingresar columna(1-10): "));
            if (fila < 1) | (fila > 10):
                print("---------------------------------------------------------------------------");
                print(f"ERROR, el numero suministrado es {fila}, por lo tanto, es invalido.");
                print("Por favor ingresar un valor entero entre 1 y 10.");
                print("---------------------------------------------------------------------------");
            elif (columna < 1) | (columna > 10):
                print("---------------------------------------------------------------------------");
                print(f"ERROR, el numero suministrado es {columna}, por lo tanto, es invalido.");
                print("Por favor ingresar un valor entero entre 1 y 10.");
                print("---------------------------------------------------------------------------");
            else:
                EliminarCelula(caldo, fila, columna);

# PROGRAMA PRINCIPAL
def main():

    ACA = False;

    print("-----------------------------------");
    print("UCAB, hecho por Freddy Fernandez.");
    print("-----------------------------------");

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
            print("---------------------------------------------------------------------------");
            print(f"ERROR, el numero suministrado es {data}, por lo tanto, es invalido.");
            print("Por favor ingresar un valor entero entre 10 y 25.");
            print("---------------------------------------------------------------------------");

        else:

            bol = True;
            copy = data;

            while (ACA == False):

                DistribuirCelulas(caldo, copy, pos);
                ImprimirCultivo(caldo);
            
                MenuOpciones(caldo);

main()