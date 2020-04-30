# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 20:03:57 2018

@author: arien
"""

import random

def crearmatriz():
    n = 8
    matriz = [[0] * n for i in range(n)]
    return matriz

def imprimirmatriz(matriz):
    n = len(matriz)
    for f in range(n):
        for c in range(n):
            print("%3d" %matriz[f][c], end="")
        print()

def colocardama(matriz):
    n = len(matriz)
    filadama = random.randint(0,7)
    coldama = random.randint(0,7)
    # Fila de la dama
    for c in range(8):
        matriz[filadama][c] = 1
    # Columna de la dama
    for f in range(8):
        matriz[f][coldama] = 1
    # Diagonal NO (Noroeste)    
    f = filadama
    c = coldama
    while f>=0 and c>=0:
        matriz[f][c] = 1
        f -= 1
        c -= 1
    # Diagonal NE (Noreste)    
    f = filadama
    c = coldama
    while f>=0 and c<n:
        matriz[f][c] = 1
        f -= 1
        c += 1
    # Diagonal SO (Sudoeste)    
    f = filadama
    c = coldama
    while f<n and c>=0:
        matriz[f][c] = 1
        f += 1
        c -= 1
    # Diagonal SE (Sudeste)    
    f = filadama
    c = coldama
    while f<n and c<n:
        matriz[f][c] = 1
        f += 1
        c += 1
    # Finalmente colocamos la dama en el tablero
    matriz[filadama][coldama] = 2

# Programa principal
mat = crearmatriz()
colocardama(mat)
imprimirmatriz(mat)
