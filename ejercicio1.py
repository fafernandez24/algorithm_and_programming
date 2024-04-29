#import ramdom
#import colorama
from colorama import*

#Solicitar un numero entero > 0 (N)
#Validar el numero "N"
#Si no hay error, mostrar los 10 primeros a partir de N de 3 en 3
#Alternar el color de los numeros entre rojo y azul

#Resolver usando ciclos WHILE y FOR por separado

#Crear un menu

init(autoreset= True)

def main():
    print(Fore.MAGENTA + "--------------------------------------");
    print(Fore.MAGENTA + "UCAB elaborado por: Freddy Fernandez.")
    print(Fore.MAGENTA + "--------------------------------------");

    n = int(input("Ingresar un numero entero mayor a 0: "));
    aux = n + 30;

    if (n > 0):
        menu = input(Fore.LIGHTCYAN_EX + "[w] Usar ciclo while --- [f] Usar ciclo for: ").lower();

        if (menu == "w"):
            while n - 3 < aux - 3:
                if (n % 2 == 0):
                    x = str(n);
                    print(Fore.RED + x);
                    n += 3;
                else:
                    x = str(n);
                    print(Fore.BLUE + x);
                    n += 3;

        elif (menu == "f"):
            for i in range(n, aux, 3):
                    if (i % 2 == 0):
                        x = str(i);
                        print(Fore.RED + x);
                    else:
                        x = str(i);
                        print(Fore.BLUE + x);
        else:
            print(Fore.RED + "Ingresar un caracter valido!");

    else:
        print(Fore.RED + "Por favor, ingresar un valor valido.");

main()