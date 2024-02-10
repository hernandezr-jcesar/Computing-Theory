# Programa 4 Buscador de palabras
# Palabras a encontrar:
# coin  eBay    home    master  page    site    web
# Web para hacer los textos
# https://www.loremipzum.com/es/generador-de-texto

import os

# Función para listar los archivos que esten en el directorio para leerlos
def listararchivos():
    ejemplo_dir = '/Users/cesar/OneDrive/Documentos/Cuarto Semestre/TEORIA DE LA COMPUTACION/Segundo Parcial/Buscador De Palabras/ProgramaPython/archivos'
    with os.scandir(ejemplo_dir) as ficheros:
        for fichero in ficheros:
            print(fichero.name)


# Función para limpiar la pantalla/consola/terminal
def limpiarpantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def guardarcadenas(numlinea,numcolumna,nombrearchivo):
    ruta = "archivos/" + nombrearchivo
    archivo = open(ruta, "a")
    archivo.write("[")
    archivo.write(str(numlinea))
    archivo.write("  ")
    archivo.write(str(numcolumna))
    archivo.write("]\n")


def automataArchivo(nombrearchivo):
    ruta = "archivos/" + nombrearchivo
    #Usando with el archivo se cierra automaticamente
    conta = 0
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            conta = conta + 1
            #print(linea)
            for i in range(0, len(linea)):
                cadena = linea
                if cadena[i] == 'c':
                    if cadena[i+1] == 'o':
                        if cadena[i+2] == 'i':
                            if cadena[i+3] == 'n':
                                if cadena[i+4] == ' ':
                                    numcolumna = i + 1
                                    numlinea = conta
                                    guardarcadenas(numlinea, numcolumna, "coin.txt")
                if cadena[i] == 'e':
                    if cadena[i+1] == 'B':
                        if cadena[i+2] == 'a':
                            if cadena[i+3] == 'y':
                                if cadena[i + 4] == ' ':
                                    numcolumna = i + 1
                                    numlinea = conta
                                    guardarcadenas(numlinea, numcolumna, "eBay.txt")
                if cadena[i] == 'h':
                    if cadena[i+1] == 'o':
                        if cadena[i+2] == 'm':
                            if cadena[i+3] == 'e':
                                if cadena[i + 4] == ' ':
                                    numcolumna = i + 1
                                    numlinea = conta
                                    guardarcadenas(numlinea, numcolumna, "home.txt")
                if cadena[i] == 'm':
                    if cadena[i+1] == 'a':
                        if cadena[i+2] == 's':
                            if cadena[i+3] == 't':
                                if cadena[i+4] == 'e':
                                    if cadena[i+5] == 'r':
                                        if cadena[i + 6] == ' ':
                                            numcolumna = i + 1
                                            numlinea = conta
                                            guardarcadenas(numlinea, numcolumna, "master.txt")
                if cadena[i] == 'p':
                    if cadena[i+1] == 'a':
                        if cadena[i+2] == 'g':
                            if cadena[i+3] == 'e':
                                if cadena[i + 4] == ' ':
                                    numcolumna = i + 1
                                    numlinea = conta
                                    guardarcadenas(numlinea, numcolumna, "page.txt")
                if cadena[i] == 's':
                    if cadena[i+1] == 'i':
                        if cadena[i+2] == 't':
                            if cadena[i+3] == 'e':
                                if cadena[i + 4] == ' ':
                                    numcolumna = i + 1
                                    numlinea = conta
                                    guardarcadenas(numlinea, numcolumna, "site.txt")
                if cadena[i] == 'w':
                    if cadena[i+1] == 'e':
                        if cadena[i+2] == 'b':
                            if cadena[i + 4] == ' ':
                                numcolumna = i + 1
                                numlinea = conta
                                guardarcadenas(numlinea, numcolumna, "web.txt")


def borrararchivos():
    if os.path.isfile("archivos/eBay.txt"):
        os.remove("archivos/eBay.txt")
    if os.path.isfile("archivos/coin.txt"):
        os.remove("archivos/coin.txt")
    if os.path.isfile("archivos/home.txt"):
        os.remove("archivos/home.txt")
    if os.path.isfile("archivos/master.txt"):
        os.remove("archivos/master.txt")
    if os.path.isfile("archivos/page.txt"):
        os.remove("archivos/page.txt")
    if os.path.isfile("archivos/site.txt"):
        os.remove("archivos/site.txt")
    if os.path.isfile("archivos/web.txt"):
        os.remove("archivos/web.txt")
    if os.path.isfile("archivos/palabrasreservadas.txt"):
        os.remove("archivos/palabrasreservadas.txt")


def contarpalabra(nombrearchivo):
    ruta = "archivos/" + nombrearchivo + ".txt"
    with open(ruta, 'r') as archivo:
        conta = 0
        for linea in archivo:
            conta = conta + 1
    return conta


def guardarlineas(nombrearchivo, file):
    ruta = "archivos/" + nombrearchivo + ".txt"

    with open(ruta) as archivo:
        file.write(nombrearchivo)
        file.write("\n")
        cantidad = contarpalabra(nombrearchivo)
        file.write("cantidad:")
        file.write(str(cantidad))
        file.write("\n[fila columna]\n")
        for linea in archivo:
            nuevalinea = ''
            for caracter in linea:
                if caracter != "\n":
                    nuevalinea = nuevalinea + caracter
            file.write(nuevalinea)
        file.write("\n")
        file.write("\n")


def juntararchivos():
    with open("archivos/palabrasreservadas.txt", "a") as file:
        guardarlineas("coin", file)
        guardarlineas("eBay", file)
        guardarlineas("home", file)
        guardarlineas("master", file)
        guardarlineas("page", file)
        guardarlineas("site", file)
        guardarlineas("web", file)


def FuncArchivo():
    # Se verifica que el archivo solicitado exista para poder continuar
    limpiarpantalla()
    print("Archivo")
    listararchivos()
    try:
        print("¿Que archivo desea evaluar? ")
        respuesta = input()
        automataArchivo(respuesta)
        juntararchivos()
        print("El archivo ha sido analizado con exito.")
    except FileNotFoundError:
        limpiarpantalla()
        print("Archivo no encontrado")
    except FileExistsError:
        limpiarpantalla()
        print("Archivo no existente")
    except:
        limpiarpantalla()
        print("Ninguna entrada")

def FuncCadena():
    limpiarpantalla()
    print("Cadena")


def menu():

    while True:
        limpiarpantalla()
        print("Menu Programa 4")
        print("1. Ingresar un Archivo de Texto")
        print("2. Ingresar una cadena")
        print("3. Salir")
        respuesta = input("Favor de escoger una opcion\n")

        if respuesta == '1':
            # Archivo()
            borrararchivos()
            FuncArchivo()
            os.system("pause")
        elif respuesta == '2':
            # Cadena()
            FuncCadena()
            os.system("pause")
        elif respuesta == '3':
            break
        else:
            print("Favor de escoger una opcion valida")
    print("Fin del Programa 4")


if __name__ == '__main__':
    menu()


