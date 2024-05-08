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
        show = print(f"| {cuadro[fila][columna]} ", end= " |");
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
        tablero[random.randint(0,9)][random.randint(0,9)] = "🟩";

# Funcion para imprimir las posiciones de las celulas.
def ImprimirPosiciones(tablero):

    fila: int;
    columna: int;

    fila = 0;
    columna = 0;

    print(Fore.CYAN + "POSICIONES - [fila][columna] ");
    while (fila <= 9):
        if (tablero[fila][columna] == "🟩"):
             print(f"[{fila + 1}][{columna + 1}]", end= " - ");
        columna += 1;
        if (columna == 9):
            fila += 1;
            columna = 0;
    print("CELULAS VIVAS");

# Funcion que permite al usuario agregar una celula en la posicion indicada.
def AgregarCelula(tablero, vertical, horizontal):
    vertical -= 1;
    horizontal -=1;

    if (tablero[vertical][horizontal] == "🟩"):
        return print(Fore.RED + f"ERROR, la posición [{vertical + 1}][{horizontal + 1}] ya esta ocupada.");
    else:
        tablero[vertical][horizontal] = "🟩";
        return tablero[vertical][horizontal];

# Funcion que permite al usuario eliminar una celula en la posicion indicada.
def EliminarCelula(tablero, vertical, horizontal):
    vertical -= 1;
    horizontal -=1;

    if (tablero[vertical][horizontal] == "⬛"):
        return print(Fore.RED + f"ERROR, la posición [{vertical + 1}][{horizontal + 1}] ya se encuentra desocupada.");
    else:
        tablero[vertical][horizontal] = "⬛";
        return tablero[vertical][horizontal];

# Menu que permite al usuario ingresar a las funciones de agregar y eliminar celula.
def MenuOpciones(tablero):

    opcion:int;
    fila: int;
    columna: int;

    print(Fore.YELLOW + "------------------------------");
    print(Fore.YELLOW + "========== OPCIONES ==========");
    print(Fore.YELLOW + "------------------------------");
    print(Fore.YELLOW + "(1) Agregar celula");
    print(Fore.YELLOW + "(2) Eliminar celula");
    print(Fore.YELLOW + "(3) Salir)");

    print(Fore.YELLOW + "-------------------");
    opcion = int(input(Fore.YELLOW + "Elegir una opcion: "));
    print(Fore.YELLOW + "-------------------");

    if (opcion == 1):

        fila = int(input(Fore.YELLOW + "Ingresar fila(1-10): "));
        columna = int(input(Fore.YELLOW + "Ingresar columna(1-10): "));

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

        fila = int(input(Fore.YELLOW + "Ingresar fila(1-10): "));
        columna = int(input(Fore.YELLOW + "Ingresar columna(1-10): "));

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
            return EliminarCelula(tablero, fila, columna);

    elif( opcion == 3):
        print(Fore.MAGENTA + "¡Hasta la vista, baby!");
        aca = True;
        return opcion;

# PROGRAMA PRINCIPAL
def main():

    aca = False;

    print(Fore.MAGENTA + "-----------------------------------");
    print(Fore.MAGENTA + "UCAB, hecho por Freddy Fernandez.");
    print(Fore.MAGENTA + "-----------------------------------");

    bol = False;
    caldo =[["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"]];
    
    while( bol == False):
        print(Fore.CYAN + "--------------------------------------------------------------------");
        data = int(input(Fore.CYAN + "Ingresar el numero de celulas vivas en el caldo entre 10 y 25: "));
        print(Fore.CYAN + "--------------------------------------------------------------------");

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
                
                print(Fore.CYAN + "============================ CULTIVO ==========================");
                ImprimirCultivo(caldo);
                print(Fore.CYAN + "===============================================================");
                ImprimirPosiciones(caldo);

                if (MenuOpciones(caldo) == 3):
                    aca = True;

main()