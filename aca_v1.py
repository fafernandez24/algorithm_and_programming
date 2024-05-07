# Librerias implementadas
import random
from colorama import init, Fore; 
init(autoreset=True)

# Declaracion de variables
aca: bool;
data: int;
copy: int;
caldo: list;
bol: bool;

# Funcion para imprimir el tablero.
def ImprimirCultivo(cuadro):
    fila: int;
    columna: int;
    show: None;

    fila = 0;
    columna = 0;

    while (fila <= 9):
        show = print(f"|{cuadro[fila][columna]}", end= "|");
        columna += 1;
        if (columna == 9):
            fila += 1;
            columna = 0;
            print("");
     
    return show;

# Funcion para validar el dato suministrado por el usuario.
def ValidarDato(valor):
    bol: bool;
    bol = False;
    if (valor < 10) | (valor > 25):
        bol = False;
    else:
        bol = True;
    return bol;

# Procedimiento para distribuir de forma aleatoria por el tablero el numero de celulas ingresadas por el usuario.
def DistribuirCelulas(tablero, dato):
    for i in range(0, dato, 1):
        tablero[random.randint(0,9)][random.randint(0,9)] = 1;

# Funcion para imprimir las posiciones de las celulas.
def ImprimirPosiciones(tablero):

    fila: int;
    columna: int;

    fila = 0;
    columna = 0;

    print(Fore.CYAN + "POSICIONES - [fila][columna] ");
    while (fila <= 9):
        if (tablero[fila][columna] == 1):
             print(f"|[{fila + 1}][{columna + 1}]", end= "|");
        columna += 1;
        if (columna == 9):
            fila += 1;
            columna = 0;
    print("");

# Funcion que permite al usuario agregar una celula en la posicion indicada.
def AgregarCelula(tablero, vertical, horizontal):
    vertical -= 1;
    horizontal -=1;


    if (tablero[vertical][horizontal] == 1):
        return print(Fore.RED + f"ERROR, la posición {tablero[vertical][horizontal]} ya esta ocupada.");
    else:
        tablero[vertical][horizontal] = 1;
        return tablero[vertical][horizontal];

# Funcion que permite al usuario eliminar una celula en la posicion indicada.
def EliminarCelula(tablero, vertical, horizontal):
    vertical -= 1;
    horizontal -=1;

    if (tablero[vertical][horizontal] == 0):
        return print(Fore.RED + f"ERROR, la posición {tablero[vertical][horizontal]} ya se encuentra desocupada.");
    else:
        tablero[vertical][horizontal] = 0;
        return tablero[vertical][horizontal];

# Menu que permite al usuario ingresar a las funciones de agregar y eliminar celula.
def MenuOpciones(tablero, aca):

    opcion:int;
    fila: int;
    columna: int;

    print("------------------------");
    print("===== OPCIONES =====");
    print("------------------------");
    print("(1) Agregar celula");
    print("(2) Eliminar celula");
    print("(3) Salir)");

    opcion = int(input("Elegir una opcion: "));

    if (opcion == 1):
        fila = int(input("Ingresar fila(1-10): "));
        columna = int(input("Ingresar columna(1-10): "));
        if (fila < 1) | (fila > 10):
            print(Fore.RED + "---------------------------------------------------------------------------------------");
            print(Fore.RED + f"ERROR, el numero suministrado es {fila}, por lo tanto, es invalido.");
            print(Fore.RED + "Por favor ingresar un valor entero entre 1 y 10 tanto en filas como en columnas.");
            print(Fore.RED + "---------------------------------------------------------------------------------------");
        elif (columna < 1) | (columna > 10):
            print(Fore.RED + "---------------------------------------------------------------------------------------");
            print(Fore.RED + f"ERROR, el numero suministrado es {columna}, por lo tanto, es invalido.");
            print(Fore.RED + "Por favor ingresar un valor entero entre 1 y 10 tanto en filas como en columnas.");
            print(Fore.RED + "---------------------------------------------------------------------------------------");
        else:
            return AgregarCelula(tablero, fila, columna);

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
            return EliminarCelula(tablero, fila, columna);

    elif( opcion == 3):
        print(Fore.YELLOW + "¡Hasta la vista, baby!");
        aca = True;
        return aca

# PROGRAMA PRINCIPAL
def main():

    aca = False;

    print(Fore.YELLOW + "-----------------------------------");
    print(Fore.YELLOW + "UCAB, hecho por Freddy Fernandez.");
    print(Fore.YELLOW + "-----------------------------------");

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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];
    
    while( bol == False):
        data = int(input(Fore.CYAN + "Ingresar el numero de celulas vivas en el caldo entre 10 y 25: "));
        
        if (ValidarDato(data) == False):
            print(Fore.RED + "---------------------------------------------------------------------------");
            print(Fore.RED + f"ERROR, el numero suministrado es {data}, por lo tanto, es invalido.");
            print(Fore.RED + "Por favor ingresar un valor entero entre 10 y 25.");
            print(Fore.RED + "---------------------------------------------------------------------------");

        else:

            bol = True;
            copy = data;

            DistribuirCelulas(caldo, copy);

            while (aca == False):
                
                print(Fore.CYAN + "========= CULTIVO =========");
                ImprimirCultivo(caldo);
                ImprimirPosiciones(caldo);

                MenuOpciones(caldo, aca);

main()
