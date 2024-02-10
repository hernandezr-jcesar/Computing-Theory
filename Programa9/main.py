# PROGRAMA 9
# Del artículo de arXiv "What can we learn from universal Turing machines?"
# Se tiene que programar la máquina de la tabla 1

#   1.La máquina se tiene que animar para cadenas pequeñas (<10 caracteres)     LISTO
#   2.Puede recibir la cadena por parte del usuario o aleatoriamente            LISTO
#   3.Mandar la salida a un archivo de texto que muestre las descripciones      LISTO
#    instantáneas por renglón en cada iteración
import os
import sys
import time
from termcolor import colored
import random


def limpiarpantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def crearcadena(izquierda, derecha):
    cad_izquierda = ""
    cad_derecha = ""
    conta = 0
    while conta < izquierda:
        cad_izquierda = cad_izquierda + '|'
        conta += 1
    conta = 0
    while conta < derecha:
        cad_derecha = cad_derecha + '|'
        conta += 1
    cadena_final = '_*' + cad_izquierda + '*' + cad_derecha + '*_'
    return cadena_final


def sustituirletra(conta, cadena, letra):
    lista = list(cadena)
    lista[conta] = letra
    cadena = ''.join(lista)
    return cadena


def TuringMachine(cadena):
    q1 = 1
    q2 = 2
    q3 = 3
    q4 = 4
    q5 = 5
    q6 = 6
    q7 = 7
    q8 = 8
    q9 = 9
    conta = 1
    estado_actual = q1
    #print(cadena, conta, estado_actual)
    historia(cadena, conta, estado_actual)
    while 1:
        if estado_actual == q1:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                cadena = sustituirletra(conta, cadena, 'X')
                conta = conta + 1
                estado_actual = q2
                historia(cadena, conta, estado_actual)
        if estado_actual == q2:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                conta += 1
                estado_actual = q3
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta += 1
                historia(cadena, conta, estado_actual)
        if estado_actual == q3:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                cadena = sustituirletra(conta, cadena, 'X')
                conta -= 1
                estado_actual = q4
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta = conta + 1
                historia(cadena, conta, estado_actual)
        if estado_actual == q4:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                conta = conta - 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                cadena = sustituirletra(conta, cadena, 'a')
                conta = conta + 1
                estado_actual = q5
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == 'X':
                conta = conta + 1
                estado_actual = q7
                historia(cadena, conta, estado_actual)
        if estado_actual == q5:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '_':
                cadena = sustituirletra(conta, cadena, '|')
                cadena = cadena + '_'
                conta = conta - 1
                estado_actual = q6
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '*':
                conta = conta + 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta = conta + 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == 'X':
                conta = conta + 1
                historia(cadena, conta, estado_actual)
        if estado_actual == q6:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                conta = conta - 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta = conta - 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == 'a':
                cadena = sustituirletra(conta, cadena, '|')
                conta = conta - 1
                estado_actual = q4
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == 'X':
                conta = conta - 1
                historia(cadena, conta, estado_actual)
        if estado_actual == q7:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                conta = conta + 1
                estado_actual = q8
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta = conta + 1
                historia(cadena, conta, estado_actual)
        if estado_actual == q8:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '_':
                cadena = sustituirletra(conta, cadena, '*')
                cadena = cadena + '_'
                conta = conta - 1
                estado_actual = q9
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta = conta + 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == 'X':
                cadena = sustituirletra(conta, cadena, '*')
                conta = conta + 1
                historia(cadena, conta, estado_actual)
        if estado_actual == q9:
            #print(cadena, conta, estado_actual)
            if cadena[conta] == '*':
                conta = conta - 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == '|':
                conta = conta - 1
                historia(cadena, conta, estado_actual)
            elif cadena[conta] == 'X':
                cadena = sustituirletra(conta, cadena, '*')
                historia(cadena, conta, estado_actual)
                #return cadena
                break

def manual():
    limpiarpantalla()
    print('Manual')
    try:
        izquierda = input('Cantidad de | del lado izquierdo:')
        derecha = input('Cantidad de | del lado derecho:')
        cadena_creada = crearcadena(int(izquierda), int(derecha))
        suma = int(izquierda) + int(derecha)
    except ValueError:
        izquier = 0
        dere = 0
        cadena_creada = crearcadena(izquier, dere)
        suma = 0
    print('Cadena creada: ', end='')
    print(cadena_creada)
    print(" ")
    tituloarchivo()
    TuringMachine(cadena_creada)
    print('Cadena evaluada, Archivo de historia creado')
    if suma <= 10:
        animacion()
    input()


def automatico():
    limpiarpantalla()
    print('Automático')
    izquierda = random.randint(0,100)
    derecha = random.randint(0,100)
    suma = izquierda + derecha
    cadena_creada = crearcadena(izquierda, derecha)
    print('Cadena creada: ', end='')
    print(cadena_creada)
    print(" ")
    tituloarchivo()
    TuringMachine(cadena_creada)
    print('Cadena evaluada, Archivo de historia creado')
    if suma <= 10:
        animacion()
    input()

def tituloarchivo():
    archivo = open("Historia.txt", "a")
    linea = "Cadena     Estado      Conta"
    archivo.write(linea)
    archivo.write("\n")
    archivo.close()


def historia(cadena, conta, estado):
    archivo = open("Historia.txt", "a")
    linea = cadena + "  " + str(estado) + "  " + str(conta)
    archivo.write(linea)
    archivo.write("\n")
    archivo.close()


def animacion():
    archivo = open("Historia.txt", "r")
    while True:
        linea = archivo.readline()
        for char in linea:
            sys.stdout.write(colored(char, 'green'))
            sys.stdout.flush()
            if char != "\n":
                time.sleep(0.1)
        if not linea:
            break
    archivo.close()


def menu():
    if os.path.isfile("Historia.txt"):
        os.remove("Historia.txt")
    while True:
        limpiarpantalla()
        print('Menu Programa 9')
        print('1.Forma Manual')
        print('2.Forma Automatica')
        print('3.Salir')
        respuesta = input('Favor de escoger una opción \n')
        if respuesta == '1':
            if os.path.isfile("Historia.txt"):
                os.remove("Historia.txt")
            manual()
        elif respuesta == '2':
            if os.path.isfile("Historia.txt"):
                os.remove("Historia.txt")
            automatico()
        elif respuesta == '3':
            break
        else:
            print('Igrese un valor entre 1 y 3')
            input()
    print('Fin del Programa')


if __name__ == '__main__':
    menu()
