# Programa3
# Tablero 4 * 4

from threading import Thread
import os
import random



def limpiarpantalla():  # Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def verificarsecuencia(secuencia):
    secuencia = secuencia + "."
    todoslosmovimientos(secuencia)
    largo = len(secuencia)
    for i in range(0, largo):
        if secuencia[i] == '1':
            if secuencia[i+1] == '6':
                if secuencia[i+2] == ' ':
                    if secuencia[i+3] == '.':
                        movimientosganadores(secuencia)


def movimientosganadores(cadena):
    archivo = open("MovimientosGanadores.txt", "a")
    archivo.write(cadena)
    archivo.write("\n")
    archivo.close()


def generarsecuencia(conta):
    secuencia = ""
    for i in range(0, conta):
        i = random.randrange(0, 2)
        if i == 0:
            secuencia = secuencia + 'r'
        elif i == 1:
            secuencia = secuencia + 'b'
    return secuencia

def todoslosmovimientos(cadena):
    archivo = open("TodosLosMovimientos.txt", "a")
    archivo.write(cadena)
    archivo.write("\n")
    archivo.close()

def manual():
    limpiarpantalla()
    print("Manual")
    cadena = input("Favor de ingresar secuencia\n")
    if len(cadena) <= 20:
        automata(cadena, 0, 0, "")
    elif len(cadena) > 20:
        print("ERROR mas de 20 caracteres en la cadena")
    print(" ")
    os.system("pause")


def automatico():
    limpiarpantalla()
    print("Automatico")
    cantcaracteres = random.randrange(0,100)
    secuencia = generarsecuencia(cantcaracteres)
    print("Secuencia generada: " + secuencia)
    automata(secuencia, 0, 0, "")
    os.system("pause")


def menu():

    if os.path.isfile("MovimientosGanadores.txt"):
        os.remove("MovimientosGanadores.txt")
    if os.path.isfile("TodosLosMovimientos.txt"):
        os.remove("TodosLosMovimientos.txt")

    while True:
        limpiarpantalla()

        print("Menu Programa 3")
        print("1.Forma manual")
        print("2.Forma automatica")
        print("3.Salir")
        respuesta = input("Favor de escoger una opción\n")

        if respuesta == '1':
            manual()
        elif respuesta == '2':
            automatico()
        elif respuesta == '3':

            break
        else:
            print("Ingrese un valor entre 1 y 3")
    print("Fin del programa")


def automata(cadena, actual, conta, camino):
    q0 = 0
    q1 = 1
    q2 = 2
    q3 = 3
    q4 = 4
    q5 = 5
    q6 = 6
    q7 = 7
    q8 = 8
    q9 = 9
    q10 = 10
    q11 = 11
    q12 = 12
    q13 = 13
    q14 = 14
    q15 = 15
    largo = len(cadena)

    camino = camino + str(actual + 1) + " "
    #print(camino)

    if conta == largo + 1:
        camino = camino + "."
        return
    verificarsecuencia(camino)





    conta = conta + 1

    if conta < largo + 1:

        # estado q0
        if actual == q0:
            if cadena[conta-1] == 'r':
                h1 = Thread(target=automata, args=(cadena, q1, conta, camino,))
                h1.start()
                h1.join()
                h2 = Thread(target=automata, args=(cadena, q4, conta, camino,))
                h2.start()
                h2.join()

            if cadena[conta-1] == 'b':
                h3 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h3.start()
                h3.join()

        # estado q1
        if actual == q1:
            if cadena[conta-1] == 'r':
                h4 = Thread(target=automata, args=(cadena, q4, conta, camino,))
                h4.start()
                h4.join()
                h5 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h5.start()
                h5.join()

            if cadena[conta-1] == 'b':
                h6 = Thread(target=automata, args=(cadena, q0, conta, camino,))
                h6.start()
                h6.join()
                h7 = Thread(target=automata, args=(cadena, q2, conta, camino,))
                h7.start()
                h7.join()
                h8 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h8.start()
                h8.join()

        # estado q2
        if actual == q2:
            if cadena[conta-1] == 'r':
                h9 = Thread(target=automata, args=(cadena, q1, conta, camino,))
                h9.start()
                h9.join()
                h10 = Thread(target=automata, args=(cadena, q3, conta, camino,))
                h10.start()
                h10.join()
                h11 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h11.start()
                h11.join()

            if cadena[conta-1] == 'b':
                h12 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h12.start()
                h12.join()
                h13 = Thread(target=automata, args=(cadena, q7, conta, camino,))
                h13.start()
                h13.join()

        # estado q3
        if actual == q3:
            if cadena[conta-1] == 'r':
                h14 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h14.start()
                h14.join()

            if cadena[conta-1] == 'b':
                h15 = Thread(target=automata, args=(cadena, q2, conta, camino,))
                h15.start()
                h15.join()
                h16 = Thread(target=automata, args=(cadena, q7, conta, camino,))
                h16.start()
                h16.join()

        # estado q4
        if actual == q4:
            if cadena[conta-1] == 'r':
                h17 = Thread(target=automata, args=(cadena, q1, conta, camino,))
                h17.start()
                h17.join()
                h18 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h18.start()
                h18.join()

            if cadena[conta-1] == 'b':
                h19 = Thread(target=automata, args=(cadena, q0, conta, camino,))
                h19.start()
                h19.join()
                h20 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h20.start()
                h20.join()
                h21 = Thread(target=automata, args=(cadena, q8, conta, camino,))
                h21.start()
                h21.join()

        # estado q5
        if actual == q5:
            if cadena[conta-1] == 'r':
                h22 = Thread(target=automata, args=(cadena, q1, conta, camino,))
                h22.start()
                h22.join()
                h23 = Thread(target=automata, args=(cadena, q4, conta, camino,))
                h23.start()
                h23.join()
                h24 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h24.start()
                h24.join()
                h25 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h25.start()
                h25.join()
            if cadena[conta-1] == 'b':
                h26 = Thread(target=automata, args=(cadena, q0, conta, camino,))
                h26.start()
                h26.join()
                h27 = Thread(target=automata, args=(cadena, q2, conta, camino,))
                h27.start()
                h27.join()
                h28 = Thread(target=automata, args=(cadena, q8, conta, camino,))
                h28.start()
                h28.join()
                h29 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h29.start()
                h29.join()
        # estado q6
        if actual == q6:
            if cadena[conta-1] == 'r':
                h30 = Thread(target=automata, args=(cadena, q1, conta, camino,))
                h30.start()
                h30.join()
                h31 = Thread(target=automata, args=(cadena, q3, conta, camino,))
                h31.start()
                h31.join()
                h32 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h32.start()
                h32.join()
                h33 = Thread(target=automata, args=(cadena, q11, conta, camino,))
                h33.start()
                h33.join()
            if cadena[conta-1] == 'b':
                h34 = Thread(target=automata, args=(cadena, q2, conta, camino,))
                h34.start()
                h34.join()
                h35 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h35.start()
                h35.join()
                h36 = Thread(target=automata, args=(cadena, q7, conta, camino,))
                h36.start()
                h36.join()
                h37 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h37.start()
                h37.join()

        # estado q7
        if actual == q7:
            if cadena[conta-1] == 'r':
                h38 = Thread(target=automata, args=(cadena, q3, conta, camino,))
                h38.start()
                h38.join()
                h39 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h39.start()
                h39.join()
                h40 = Thread(target=automata, args=(cadena, q11, conta, camino,))
                h40.start()
                h40.join()
            if cadena[conta-1] == 'b':
                h41 = Thread(target=automata, args=(cadena, q2, conta, camino,))
                h41.start()
                h41.join()
                h42 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h42.start()
                h42.join()
        # estado q8
        if actual == q8:
            if cadena[conta-1] == 'r':
                h43 = Thread(target=automata, args=(cadena, q4, conta, camino,))
                h43.start()
                h43.join()
                h44 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h44.start()
                h44.join()
                h45 = Thread(target=automata, args=(cadena, q12, conta, camino,))
                h45.start()
                h45.join()
            if cadena[conta-1] == 'b':
                h46 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h46.start()
                h46.join()
                h47 = Thread(target=automata, args=(cadena, q13, conta, camino,))
                h47.start()
                h47.join()
        # estado q9
        if actual == q9:
            if cadena[conta-1] == 'r':
                h48 = Thread(target=automata, args=(cadena, q4, conta, camino,))
                h48.start()
                h48.join()
                h49 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h49.start()
                h49.join()
                h50 = Thread(target=automata, args=(cadena, q12, conta, camino,))
                h50.start()
                h50.join()
                h51 = Thread(target=automata, args=(cadena, q14, conta, camino,))
                h51.start()
                h51.join()

            if cadena[conta-1] == 'b':
                h52 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h52.start()
                h52.join()
                h53 = Thread(target=automata, args=(cadena, q8, conta, camino,))
                h53.start()
                h53.join()
                h54 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h54.start()
                h54.join()
                h55 = Thread(target=automata, args=(cadena, q13, conta, camino,))
                h55.start()
                h55.join()

        # estado q10
        if actual == q10:
            if cadena[conta-1] == 'r':
                h56 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h56.start()
                h56.join()
                h57 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h57.start()
                h57.join()
                h58 = Thread(target=automata, args=(cadena, q11, conta, camino,))
                h58.start()
                h58.join()
                h59 = Thread(target=automata, args=(cadena, q14, conta, camino,))
                h59.start()
                h59.join()
            if cadena[conta-1] == 'b':
                h60 = Thread(target=automata, args=(cadena, q5, conta, camino,))
                h60.start()
                h60.join()
                h61 = Thread(target=automata, args=(cadena, q7, conta, camino,))
                h61.start()
                h61.join()
                h62 = Thread(target=automata, args=(cadena, q13, conta, camino,))
                h62.start()
                h62.join()
                h63 = Thread(target=automata, args=(cadena, q15, conta, camino,))
                h63.start()
                h63.join()
        # estado q11
        if actual == q11:
            if cadena[conta-1] == 'r':
                h64 = Thread(target=automata, args=(cadena, q6, conta, camino,))
                h64.start()
                h64.join()
                h65 = Thread(target=automata, args=(cadena, q14, conta, camino,))
                h65.start()
                h65.join()

            if cadena[conta-1] == 'b':
                h67 = Thread(target=automata, args=(cadena, q7, conta, camino,))
                h67.start()
                h67.join()
                h68 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h68.start()
                h68.join()
                h69 = Thread(target=automata, args=(cadena, q15, conta, camino,))
                h69.start()
                h69.join()

        # estado q12
        if actual == q12:
            if cadena[conta-1] == 'r':
                h70 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h70.start()
                h70.join()

            if cadena[conta-1] == 'b':
                h71 = Thread(target=automata, args=(cadena, q8, conta, camino,))
                h71.start()
                h71.join()
                h72 = Thread(target=automata, args=(cadena, q13, conta, camino,))
                h72.start()
                h72.join()

        # estado q13
        if actual == q13:
            if cadena[conta-1] == 'r':
                h73 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h73.start()
                h73.join()
                h74 = Thread(target=automata, args=(cadena, q12, conta, camino,))
                h74.start()
                h74.join()
                h75 = Thread(target=automata, args=(cadena, q14, conta, camino,))
                h75.start()
                h75.join()

            if cadena[conta-1] == 'b':
                h76 = Thread(target=automata, args=(cadena, q8, conta, camino,))
                h76.start()
                h76.join()
                h77 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h77.start()
                h77.join()
        # estado q14
        if actual == q14:
            if cadena[conta-1] == 'r':
                h78 = Thread(target=automata, args=(cadena, q9, conta, camino,))
                h78.start()
                h78.join()
                h79 = Thread(target=automata, args=(cadena, q11, conta, camino,))
                h79.start()
                h79.join()
            if cadena[conta-1] == 'b':
                h80 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h80.start()
                h80.join()
                h81 = Thread(target=automata, args=(cadena, q13, conta, camino,))
                h81.start()
                h81.join()
                h82 = Thread(target=automata, args=(cadena, q15, conta, camino,))
                h82.start()
                h82.join()
        # estado q15
        if actual == q15:
            if cadena[conta-1] == 'r':
                h83 = Thread(target=automata, args=(cadena, q11, conta, camino,))
                h83.start()
                h83.join()
                h84 = Thread(target=automata, args=(cadena, q14, conta, camino,))
                h84.start()
                h84.join()

            if cadena[conta-1] == 'b':
                h85 = Thread(target=automata, args=(cadena, q10, conta, camino,))
                h85.start()
                h85.join()


if __name__ == '__main__':
    menu()
