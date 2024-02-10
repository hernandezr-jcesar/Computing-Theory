# Programa 4 Buscador de palabras
# Palabras a encontrar:
# coin  eBay    home    master  page    site    web
# Web para hacer los textos
# https://www.loremipzum.com/es/generador-de-texto

import os
import cv2
import matplotlib.pyplot as plt

def automata(cadena, linea):
    largo = len(cadena)
    a = 1
    b = 2
    c = 6
    d = 10
    e = 14
    f = 20
    g = 24
    h = 28
    i = 3
    j = 7
    k = 11
    l = 15
    m = 21
    n = 25
    enie = 29
    o = 4
    p = 8
    q = 12
    r = 16
    s = 22
    t = 26
    u = 30
    v = 5
    w = 9
    x = 13
    y = 17
    z = 23
    _a_ = 27
    _b_ = 18
    _c_ = 19
    actual = a
    conta = 0

    columna = 0
    while True:
        columna = columna + 1
        #print(actual)
        if conta >= largo:
            break
        # Estado A
        if actual == a:
            if cadena[conta] == 'c':
                historia('B', 'A', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'A', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'A', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'A', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'A', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'A', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'A', 'w')
                actual = h
            else:
                historia('A', 'A', cadena[conta])
                actual = a
        # Estado B
        elif actual == b:
            if cadena[conta] == 'o':
                historia('I', 'B', 'o')
                actual = i
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'B', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'B', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'B', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'B', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'B', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'B', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'B', 'w')
                actual = h
            else:
                historia('A', 'B', cadena[conta])
                actual = a
        # Estado C
        elif actual == c:
            if cadena[conta] == 'b':
                historia('J', 'C', 'b')
                actual = j
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'C', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'C', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'C', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'C', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'C', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'C', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'C', 'w')
                actual = h
            else:
                historia('A', 'C', cadena[conta])
                actual = a
        # Estado D
        elif actual == d:
            if cadena[conta] == 'o':
                historia('K', 'D', 'o')
                actual = k
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'D', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'D', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'D', 'o')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'D', 'o')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'D', 'o')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'D', 'o')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'D', 'o')
                actual = h
            else:
                historia('A', 'D', cadena[conta])
                actual = a
        # Estado E
        elif actual == e:
            if cadena[conta] == 'a':
                historia('L', 'E', 'a')
                actual = l
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'E', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'E', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'E', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'E', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'E', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'E', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'E', 'w')
                actual = h
            else:
                historia('A', 'E', cadena[conta])
                actual = a
        # Estado F
        elif actual == f:
            if cadena[conta] == 'a':
                historia('M', 'F', 'a')
                actual = m
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'F', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'F', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'F', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'F', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'F', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'F', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'F', 'w')
                actual = h
            else:
                historia('A', 'F', cadena[conta])
                actual = a
        # Estado G
        elif actual == g:
            if cadena[conta] == 'i':
                historia('N', 'G', 'i')
                actual = n
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'G', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'G', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'G', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'G', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'G', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'G', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'G', 'w')
                actual = h
            else:
                historia('A', 'G', cadena[conta])
                actual = a
        # Estado H
        elif actual == h:
            if cadena[conta] == 'e':
                historia('enie', 'H', 'e')
                actual = enie
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'H', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'H', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'H', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'H', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'H', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'H', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'H', 'w')
                actual = h
            else:
                historia('A', 'H', cadena[conta])
                actual = a
        # Estado I
        elif actual == i:
            if cadena[conta] == 'i':
                historia('O', 'I', 'i')
                actual = o
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'I', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'I', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'I', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'I', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'I', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'I', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'I', 'w')
                actual = h
            else:
                historia('A', 'I', cadena[conta])
                actual = a
        # Estado J
        elif actual == j:
            if cadena[conta] == 'a':
                historia('P', 'J', 'a')
                actual = p
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'J', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'J', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'J', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'J', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'J', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'J', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'J', 'w')
                actual = h
            else:
                historia('A', 'J', cadena[conta])
                actual = a
        # Estado K
        elif actual == k:
            if cadena[conta] == 'm':
                historia('Q', 'K', 'm')
                actual = q
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'K', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'K', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'K', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'K', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'K', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'K', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'K', 'w')
                actual = h
            else:
                historia('A', 'K', cadena[conta])
                actual = a
        # Estado L
        elif actual == l:
            if cadena[conta] == 's':
                historia('R', 'L', 's')
                actual = r
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'L', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'L', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'L', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'L', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'L', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'L', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'L', 'w')
                actual = h
            else:
                historia('A', 'L', cadena[conta])
                actual = a
        # Estado M
        elif actual == m:
            if cadena[conta] == 'g':
                historia('S', 'M', 'g')
                actual = s
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'M', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'M', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'M', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'M', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'M', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'M', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'M', 'w')
                actual = h
            else:
                historia('A', 'M', cadena[conta])
                actual = a
        # Estado N
        elif actual == n:
            if cadena[conta] == 't':
                historia('T', 'N', 't')
                actual = t
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'N', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'N', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'N', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'N', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'N', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'N', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'N', 'w')
                actual = h
            else:
                historia('A', 'N', cadena[conta])
                actual = a
        # Estado Enie
        elif actual == enie:
            if cadena[conta] == 'b':
                historia('U', 'enie', 'b')
                actual = u
                guardarcadenas(linea, columna - 2, "web.txt")
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'enie', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'enie', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'enie', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'enie', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'enie', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'enie', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'enie', 'w')
                actual = h
            else:
                historia('A', 'enie', cadena[conta])
                actual = a
        # Estado O
        elif actual == o:
            if cadena[conta] == 'n':
                historia('V', 'O', 'n')
                actual = v
                guardarcadenas(linea, columna - 3, "coin.txt")
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'O', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'O', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'O', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'O', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'O', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'O', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'O', 'w')
                actual = h
            else:
                historia('A', 'O', cadena[conta])
                actual = a
        # Estado P
        elif actual == p:
            if cadena[conta] == 'y':
                historia('W', 'P', 'y')
                actual = w
                guardarcadenas(linea, columna - 3, "ebay.txt")
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'P', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'P', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'P', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'P', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'P', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'P', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'P', 'w')
                actual = h
            else:
                historia('A', 'P', cadena[conta])
                actual = a
        # Estado Q
        elif actual == q:
            if cadena[conta] == 'e':
                historia('X', 'Q', 'e')
                actual = x
                guardarcadenas(linea, columna - 3, "home.txt")
            # -------------------------
            elif cadena[conta] == 'a':
                historia('L', 'Q', 'a')
                actual = l
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'Q', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'Q', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'Q', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'Q', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'Q', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'Q', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'Q', 'w')
                actual = h
            else:
                historia('A', 'Q', cadena[conta])
                actual = a
        # Estado R
        elif actual == r:
            if cadena[conta] == 't':
                historia('Y', 'R', 't')
                actual = y
            # -------------------------
            elif cadena[conta] == 'i':
                historia('N', 'R', 'i')
                actual = n
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'R', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'R', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'R', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'R', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'R', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'R', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'R', 'w')
                actual = h
            else:
                historia('A', 'R', cadena[conta])
                actual = a
        # Estado S
        elif actual == s:
            if cadena[conta] == 'e':
                historia('Z', 'S', 'e')
                actual = z
                guardarcadenas(linea, columna - 3, "page.txt")
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'S', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'S', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'S', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'S', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'S', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'S', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'S', 'w')
                actual = h
            else:
                historia('A', 'S', cadena[conta])
                actual = a
        # Estado T
        elif actual == t:
            if cadena[conta] == 'e':
                historia("A'", 'T', 'e')
                actual = _a_
                guardarcadenas(linea, columna - 3, "site.txt")
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'T', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'T', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'T', 'c')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'T', 'c')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'T', 'c')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'T', 'c')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'T', 'c')
                actual = h
            else:
                historia('A', 'T', cadena[conta])
                actual = a
        # Estado U
        elif actual == u:
            if cadena[conta] == 'a':
                historia('P', 'U', 'a')
                actual = p
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'U', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'U', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'U', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'U', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'U', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'U', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'U', 'w')
                actual = h
            else:
                historia('A', 'U', cadena[conta])
                actual = a
        # Estado V
        elif actual == v:
            if cadena[conta] == 'c':
                historia('B', 'V', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'V', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'V', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'V', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'V', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'V', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'V', 'w')
                actual = h
            else:
                historia('A', 'V', cadena[conta])
                actual = a
        # Estado W
        elif actual == w:
            if cadena[conta] == 'c':
                historia('B', 'W', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'W', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'W', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'W', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'W', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'W', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'W', 'w')
                actual = h
            else:
                historia('A', 'W', cadena[conta])
                actual = a
        # Estado X
        elif actual == x:
            if cadena[conta] == 'b':
                historia('J', 'X', 'b')
                actual = j
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'X', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'X', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'X', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'X', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'X', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'X', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'X', 'w')
                actual = h
            else:
                historia('A', 'X', cadena[conta])
                actual = a
        # Estado Y
        elif actual == y:
            if cadena[conta] == 'e':
                historia("B'", 'Y', 'e')
                actual = _b_
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'Y', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'Y', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'Y', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'Y', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'Y', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'Y', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'Y', 'w')
                actual = h
            else:
                historia('A', 'Y', cadena[conta])
                actual = a
        # Estados Z
        elif actual == z:
            if cadena[conta] == 'b':
                historia('J', 'Z', 'b')
                actual = j
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', 'Z', 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', 'Z', 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', 'Z', 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', 'Z', 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', 'Z', 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', 'Z', 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', 'Z', 'w')
                actual = h
            else:
                historia('A', 'Z', cadena[conta])
                actual = a
        # Estados A'
        elif actual == _a_:
            if cadena[conta] == 'b':
                historia('J', "A'", 'b')
                actual = j
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', "A'", 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', "A'", 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', "A'", 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', "A'", 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', "A'", 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', "A'", 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', "A'", 'w')
                actual = h
            else:
                historia('A', "A'", cadena[conta])
                actual = a
        # Estado B'
        elif actual == _b_:
            if cadena[conta] == 'r':
                historia("C'", "B'", 'r')
                actual = _c_
                guardarcadenas(linea, columna - 5, "master.txt")
            # -------------------------
            elif cadena[conta] == 'b':
                historia('J', "B'", 'b')
                actual = j
            # -------------------------
            elif cadena[conta] == 'c':
                historia('B', "B'", 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', "B'", 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', "B'", 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', "B'", 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', "B'", 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', "B'", 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', "B'", 'w')
                actual = h
            else:
                historia('A', "B'", cadena[conta])
                actual = a
        # Estado C'
        elif actual == _c_:
            if cadena[conta] == 'c':
                historia('B', "C'", 'c')
                actual = b
            elif cadena[conta] == 'e':
                historia('C', "C'", 'e')
                actual = c
            elif cadena[conta] == 'h':
                historia('D', "C'", 'h')
                actual = d
            elif cadena[conta] == 'm':
                historia('E', "C'", 'm')
                actual = e
            elif cadena[conta] == 'p':
                historia('F', "C'", 'p')
                actual = f
            elif cadena[conta] == 's':
                historia('G', "C'", 's')
                actual = g
            elif cadena[conta] == 'w':
                historia('H', "C'", 'w')
                actual = h
            else:
                historia('A', "C'", cadena[conta])
                actual = a
        conta = conta + 1

def archivohistoria():
    archivo = open("archivos/archivohistoria.txt", "w")
    archivo.write("HISTORIA")
    archivo.write("\n")
    archivo.write("{(letra actual)[estado actual]->[estado siguiente]}")
    archivo.write("\n")
    with open("archivos/historia.txt") as historia:
        for linea in historia:
            archivo.write(linea)
    archivo.close()


def historia(estsiguiente, estactual, letra):
    archivo = open("archivos/historia.txt", "a")
    linea = "{(" + letra + ")[" + estactual + "]->[" + estsiguiente + "]}"
    archivo.write(linea)
    archivo.write("\n")
    archivo.close()


# Función para listar los archivos que esten en el directorio para leerlos
def listararchivos():
    ejemplo_dir = '/Users/cesar/OneDrive/Documentos/Cuarto Semestre/TEORIA DE LA COMPUTACION/Segundo Parcial/Buscador De Palabras/ProgramaFinal/archivos'
    with os.scandir(ejemplo_dir) as ficheros:
        for fichero in ficheros:
            print(fichero.name)


# Función para limpiar la pantalla/consola/terminal
def limpiarpantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def guardarcadenas(numlinea, numcolumna, nombrearchivo):
    ruta = "archivos/" + nombrearchivo
    archivo = open(ruta, "a")
    archivo.write("[")
    archivo.write(str(numlinea))
    archivo.write("  ")
    archivo.write(str(numcolumna))
    archivo.write("]\n")
    archivo.close()


def automataArchivo(nombrearchivo):
    ruta = "archivos/" + nombrearchivo
    # Usando with el archivo se cierra automaticamente
    conta = 0
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            conta = conta + 1
            automata(linea, conta)
            # print(linea)


def borrararchivos():
    if os.path.isfile("archivos/ebay.txt"):
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
    if os.path.isfile("archivos/historia.txt"):
        os.remove("archivos/historia.txt")



def contarpalabra(nombrearchivo):
    ruta = "archivos/" + nombrearchivo + ".txt"
    with open(ruta, 'r') as archivo:
        conta = 0
        for linea in archivo:
            conta = conta + 1
    return conta


def guardarlineas(nombrearchivo, file):
    ruta = "archivos/" + nombrearchivo + ".txt"
    if os.path.isfile(ruta):
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
        guardarlineas("ebay", file)
        guardarlineas("home", file)
        guardarlineas("master", file)
        guardarlineas("page", file)
        guardarlineas("site", file)
        guardarlineas("web", file)


def FuncArchivo():
    if os.path.isfile("archivos/historia.txt"):
        os.remove("archivos/historia.txt")
    # Se verifica que el archivo solicitado exista para poder continuar
    limpiarpantalla()
    print("Archivo")
    listararchivos()
    try:
        print("¿Que archivo desea evaluar? ")
        respuesta = input()
        automataArchivo(respuesta)
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
    if os.path.isfile("archivos/historia.txt"):
        os.remove("archivos/historia.txt")
    print("Cadena")
    try:
        print("Ingrese la cadena a evaluar: ")
        respuesta = input()
        automata(respuesta, 1)
        print("La cadena ha sido analizada con exito.")
    except:
        limpiarpantalla()
        print("Ninguna entrada")


def menu():
    while True:

        limpiarpantalla()
        print("Menu Programa 4")
        print("1. Ingresar un Archivo de Texto")
        print("2. Ingresar una cadena")
        print("3. Ver el Grafo del Programa")
        print("4. Salir")
        respuesta = input("Favor de escoger una opcion\n")

        if respuesta == '1':
            # Archivo()
            if os.path.isfile("archivos/palabrasreservadas.txt"):
                os.remove("archivos/palabrasreservadas.txt")
            if os.path.isfile("archivos/archivohistoria.txt"):
                os.remove("archivos/archivohistoria.txt")
            borrararchivos()
            FuncArchivo()
            juntararchivos()
            archivohistoria()
            borrararchivos()
            os.system("pause")
        elif respuesta == '2':
            # Cadena()
            if os.path.isfile("archivos/palabrasreservadas.txt"):
                os.remove("archivos/palabrasreservadas.txt")
            if os.path.isfile("archivos/archivohistoria.txt"):
                os.remove("archivos/archivohistoria.txt")
            borrararchivos()
            FuncCadena()
            juntararchivos()
            archivohistoria()
            borrararchivos()
            os.system("pause")
        elif respuesta == '3':
            #GRAFO
            print("Grafo del Programa")
            # Cargar la imagen con openCV
            imgBGR = cv2.imread("archivos/GrafoConLetras.png")
            # Cambiar esacio de color BGR a RGB
            imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
            # Mostrar imagen
            plt.xticks([]), plt.yticks([])
            plt.imshow(imgRGB, cmap='gray', interpolation='bicubic')
            plt.show()

        elif respuesta == '4':
            break
        else:
            print("Favor de escoger una opcion valida")

    print("Fin del Programa 4")


if __name__ == '__main__':
    menu()
