#   Programa 7 - palindromes
#   Programa que construya palindromes de un lenguaje binario
#   ENTRADA: Longitud del palindrome a generar (MAX 100,000)
#   SALIDA: Un archivo de texto especificando
#           regla_usada     cadena_resultante   hasta llegar a la cadena final
#   Debe tener opción manual y opción automatica
"""
    REGLAS DE PRODUCCIÓN PARA
    GRAMATICA LIBRE DE CONTEXTO
    QUE CONSTRUYE PALINDROMES
    (1)P->e
    (2)P->0
    (3)P->1
    (4)P->0P0
    (5)P->1P1
"""
import random
import os

def cincuenta_cincuenta():
    numero = random.randint(0, 1)
    return numero

def sustituircaracter(conta, cadena, letra):
    lista = list(cadena)
    lista[conta] = letra
    cadena = ''.join(lista)
    return cadena

def sustitur_p(cadena, regla):
    if regla == 1:
        lugar = cadena.find('P')
        i = 0
        izquierda = ""
        while i < lugar:
            izquierda = izquierda + cadena[i]
            i += 1
        # print(izquierda)
        j = lugar + 1
        derecha = ""
        while j < len(cadena):
            derecha = derecha + cadena[j]
            j += 1
        # print(derecha)
        cadena = izquierda + derecha
        # print(cadena)
        return cadena
    elif regla == 2:
        lugar = cadena.find('P')
        cadena = sustituircaracter(lugar, cadena, '0')
        # print(cadena)
        return cadena
    elif regla == 3:
        lugar = cadena.find('P')
        cadena = sustituircaracter(lugar, cadena, '1')
        # print(cadena)
        return cadena
    elif regla == 4:
        lugar = cadena.find('P')
        i = 0
        izquierda = ""
        while i < lugar:
            izquierda = izquierda + cadena[i]
            i +=1
        #print(izquierda)
        j = lugar + 1
        derecha = ""
        while j < len(cadena):
            derecha = derecha + cadena[j]
            j += 1
        #print(derecha)
        cadena = izquierda + "0P0" + derecha
        # print(cadena)
        return cadena
    elif regla == 5:
        lugar = cadena.find('P')
        i = 0
        izquierda = ""
        while i < lugar:
            izquierda = izquierda + cadena[i]
            i += 1
        # print(izquierda)
        j = lugar + 1
        derecha = ""
        while j < len(cadena):
            derecha = derecha + cadena[j]
            j += 1
        # print(derecha)
        cadena = izquierda + "1P1" + derecha
        #print(cadena)
        return cadena


def tituloarchivo():
    archivo = open("Historia.txt", "a")
    linea = "(REGLA)-> CADENA"
    archivo.write(linea)
    archivo.write('\n')
    archivo.close()


def historia(cadena, regla):
    archivo = open ('Historia.txt', 'a')
    linea = '(' + str(regla) +')->' + cadena
    archivo.write(linea)
    archivo.write('\n')
    archivo.close()

def crear_palindrome(longitud):
    #   Si es par ->    iteraciones = n/2  + e al final (regla 1)
    #   Si es impar ->  iteraciones = n/2 + alguna regla de 2 o 3
    cadena = ""
    conta = 0
    mitad = longitud / 2
    if longitud % 2 == 0: #par
        while conta < mitad:
            decision = cincuenta_cincuenta()
            if decision == 0:
                #Regla 4
                cadena = sustitur_p(cadena, 4)
                historia(cadena, 4)
            else:
                #Regla 5
                cadena = sustitur_p(cadena, 5)
                historia(cadena, 5)
            #print(cadena)
            conta += 1
        cadena = sustitur_p(cadena, 1)
        historia(cadena, 1)
        #print(cadena)
        return(cadena)
    else:#impar
        if longitud == 1:
            uno = cincuenta_cincuenta()
            if uno == 0:
                # Regla 2
                cadena = '0'
                historia(cadena, 2)
            else:
                # Regla 3
                cadena = '1'
                historia(cadena, 3)
        else:
            while conta < int(mitad):
                decision = cincuenta_cincuenta()
                if decision == 0:
                    #Regla 4
                    cadena = sustitur_p(cadena, 4)
                    historia(cadena, 4)
                else:
                    #Regla 5
                    cadena = sustitur_p(cadena, 5)
                    historia(cadena, 5)
                #print(cadena)
                conta += 1
            decision_final = cincuenta_cincuenta()
            if decision_final == 0:
                # Regla 2
                cadena = sustitur_p(cadena, 2)
                historia(cadena, 2)
            else:
                # Regla 3
                cadena = sustitur_p(cadena, 3)
                historia(cadena, 3)
        #print(cadena)
        return cadena


def limpiarpantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def manual():
    limpiarpantalla()
    print('Manual')
    tituloarchivo()
    try:
        longitud = input('¿De qué longitud se requiere el palindrome?\n')
        palindrome = crear_palindrome(int(longitud))
        print('Palindrome creado:')
        print(palindrome)
        print('Archivo Historia Creado')
        input()
    except ValueError:
        print('Ningun Valor recibido, intentar nuevamente')
        input()

def automatico():
    limpiarpantalla()
    print('Automatico')
    tituloarchivo()
    longitud = random.randint(0, 100000)
    print('El palindrome tendra una longitud de:')
    print(longitud)
    palindrome = crear_palindrome(longitud)
    print('Palindrome creado:')
    print(palindrome)
    print('Archivo Historia Creado')
    input()


def menu():
    if os.path.isfile("Historia.txt"):
        os.remove("Historia.txt")
    while True:
        limpiarpantalla()
        print('Menu programa 7')
        print('1.Forma Manual')
        print('2.Forma Automatica')
        print('3.Salir')
        respuesta = input('Favor de escoger una opcion \n')
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
            print('Ingrese un valore entre 1 y 3')
            input()
    print('Fin del programa')


if __name__ == '__main__':
    menu()


