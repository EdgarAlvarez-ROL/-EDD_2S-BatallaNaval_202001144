from cgitb import text
from glob import glob
from heapq import nsmallest
from pickle import GLOBAL
from sre_parse import State
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox, ttk
from tkinter import messagebox as mb

import random
import os
from graphviz import Digraph, Graph

# import numpy as np 

#Variables Globales
nick = ""
password = ""


FILAS = 24
COLUMNAS = 24
MAR = " "
SUBMARINO = "S"  # Ocupa una celda
DESTRUCTOR = "D"  # Ocupa dos celdas
PRUEBA = "P"
DESTRUCTOR_VERTICAL = "A"  # Ocupa dos celdas
DISPARO_FALLADO = "-"
DISPARO_ACERTADO = "*"
DISPAROS_INICIALES = 2
CANTIDAD_BARCOS_INICIALES = 1
JUGADOR_1 = "J1"
JUGADOR_2 = "J2"

barcos_una_celda = 0
barcos_dos_celda = 0
barcos_tres_celda = 0
barcos_cuatro_celda = 0


# Nombre de la ventana
root = Tk(className='Ventana de ejemplo')

#dando el tamaño a la ventana
root.geometry("500x400")
root.resizable (0,0) #Evitar que los usuarios ajusten el tamaño.


# Funciones para los Botones
def pagJuego():
    juego = Tk(className='GAME')
    juego.geometry("800x500")
    juego.resizable (0,0) #Evitar que los usuarios ajusten el tamaño.
    # matrizBarcos=Matriz()

    #Etiquetas 
    Label(juego, text="Ingrese el valor de la dimension del tablero").place(x=10, y=75)
    etiqueta = ttk.Label(juego, text="")
    etiqueta.place(x=10, y=320)
    # Label(juego, text="Ingrese su Usuario").place(x=40, y=100)
    
    #Caja de Texso
    caja1 = ttk.Entry(juego)
    caja1.place(x=10, y=100)
    caja1.insert(0,"10")
    
    
    
    # campo = ttk.Entry(juego)
    # campo.place(x=250, y=20, width=450, height=450)
    
    
    
    def nCuadricula(): 
        m = int(caja1.get())
        if (m<10):
            etiqueta['text'] = "Las dimensiones del tablero deben ser mayores a 10"
            # mb.showerror("Cuidado","No puede dejar los cuadros de entrada de números vacíos")
        elif (m==10):
            etiqueta['text'] = "Bien"
            nPortaaviones = 1
            nSubmarinos = 2 
            nDestructores = 3 
            nBuques = 4

            cantidad_barcos = nPortaaviones + nSubmarinos + nDestructores + nBuques
            configurar_cantidad_barcos(nBuques, nDestructores, nSubmarinos, nPortaaviones, cantidad_barcos, m)
            
            matriz = obtener_matriz_inicial()
            matriz = colocar_e_imprimir_barcos(matriz, cantidad_barcos, JUGADOR_1)
            imprimir_matriz(matriz, True, JUGADOR_1)
        elif (m<= 20 and m>10):
            etiqueta['text'] = "Bien"
            nPortaaviones = 2
            nSubmarinos = 4
            nDestructores = 6
            nBuques = 8

            cantidad_barcos = nPortaaviones + nSubmarinos + nDestructores + nBuques
            configurar_cantidad_barcos(nBuques, nDestructores, nSubmarinos, nPortaaviones, cantidad_barcos, m)
            
            matriz = obtener_matriz_inicial()
            matriz = colocar_e_imprimir_barcos(matriz, cantidad_barcos, JUGADOR_1)
            imprimir_matriz(matriz, True, JUGADOR_1)
        elif (m>=20):
            etiqueta['text'] = "Todo Bien"
            b_m = ((m-1)/10)+1
            # print (int(b_m))
            nPortaaviones = (int(b_m))
            nSubmarinos = nPortaaviones + (int(b_m))
            nDestructores = nSubmarinos + (int(b_m))
            nBuques = nDestructores + (int(b_m))

            
            cantidad_barcos = nPortaaviones + nSubmarinos + nDestructores + nBuques
            configurar_cantidad_barcos(nBuques, nDestructores, nSubmarinos, nPortaaviones, cantidad_barcos, m)
            
            matriz = obtener_matriz_inicial()
            matriz = colocar_e_imprimir_barcos(matriz, cantidad_barcos, JUGADOR_1)
            imprimir_matriz(matriz, True, JUGADOR_1)
           
    #Botones
    # botonDimen =  ttk.Button(juego, text="Ingresar Dimensiones", state="normal", command=estadoBoton(int(caja1.get())))
    Button(juego, text="Crear Tablero", command=nCuadricula).place(x=10,y=300)
    
    
    



def pagAdmin():
    v_admiin = Tk(className='admin')
    v_admiin.geometry("600x400")
    v_admiin.resizable (0,0) #Evitar que los usuarios ajusten el tamaño.

    #Botones
    Button(v_admiin, text="Ver usuarios en el sistema").place(x=200,y=300)


def Ingresar():
    nick = caja1.get()
    password =  caja2.get()
    # print(password)
    # print(nick)

    if ((nick.strip()) == "EDD" and (password.strip()) == "edd123"):
        #Iniciando la seccion del ADMIN
        pagAdmin()

        #Cerrando la Ventana de LOGIN
        root.destroy()
    elif ((nick.strip()) == "1" and (password.strip()) == "1"):
        pagJuego()

        #Cerrando la Ventana de LOGIN
        root.destroy()
    else:
        print("contraseña o usuario incorrecto")
    # root.destroy()
    
    

#Etiquetas 
Label(root, text="LOGIN").place(x=220, y=20)
Label(root, text="Ingrese su Usuario").place(x=40, y=100)
Label(root, text="Ingrese su Contraseña").place(x=40, y=220)

#Caja de Texto
# caja1=tk.Text(root, height=1, width=20)
# caja1.pack(padx=0, pady=100)
# caja1.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# caja2=tk.Text(root, height=1, width=20)
# caja2.pack(padx=0, pady=0)

caja1 = ttk.Entry(root)
caja1.place(x=200, y=100)

caja2 = ttk.Entry(root)
caja2.place(x=200, y=220)


#Botones
Button(root, text="INGRESAR", command=Ingresar).place(x=200,y=300)



# Funciones para crear la matriz con barcos
def obtener_matriz_inicial():
    matriz = []
    for y in range(FILAS):
        # Agregamos un arreglo a la matriz, que sería una fila básicamente
        matriz.append([])
        for x in range(COLUMNAS):
            # Y luego agregamos una celda a esa fila. Por defecto lleva "Mar"
            matriz[y].append(MAR)
    return matriz

def configurar_cantidad_barcos(nBuques, nDestructores, nSubmarinos, nPortaaviones, cantidad, m):
    global barcos_una_celda, barcos_dos_celda, barcos_tres_celda, barcos_cuatro_celda, CANTIDAD_BARCOS_INICIALES, FILAS, COLUMNAS
    barcos_una_celda = nBuques
    barcos_dos_celda = nDestructores
    barcos_tres_celda = nSubmarinos
    barcos_cuatro_celda = nPortaaviones
    CANTIDAD_BARCOS_INICIALES = cantidad
    FILAS = m
    COLUMNAS = m



def incrementar_letra(letra):
    return chr(ord(letra)+1)


def imprimir_separador_horizontal():
    # Imprimir un renglón dependiendo de las columnas
    for _ in range(COLUMNAS+1):
        print("+---", end="")
    print("+")
    


def imprimir_fila_de_numeros():
    print("|   ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print("|")


# Indica si una coordenada de la matriz está vacía
def es_mar(x, y, matriz):
    return matriz[y][x] == MAR


def coordenada_en_rango(x, y):
    return x >= 0 and x <= COLUMNAS-1 and y >= 0 and y <= FILAS-1


def colocar_e_imprimir_barcos(matriz, cantidad_barcos, jugador):
    global barcos_una_celda, barcos_dos_celda, barcos_tres_celda, barcos_cuatro_celda
    
    # Dividimos y redondeamos a entero hacia abajo (ya que no podemos colocar una parte no entera de un barco)

    # ePortaaviones = "P" # 4 CASILLAS
    # eSubmarinos = "S"   # 3 CASILLAS
    # eDestructores = "D" # 2 CASILLAS
    # eBuques = "B"       # 1 CASILLA

    b3v = barcos_tres_celda/2
    b2v = barcos_dos_celda/3
    # print("nBuques: " + str(barcos_una_celda))   
    print(CANTIDAD_BARCOS_INICIALES)

    """INSERTAR BARCOS A LA MATRIX"""
    # Primero colocamos los de dos celdas para que se acomoden bien
    # 
    matriz = colocar_barcos_de_cuatro_celdas_horizontal(
        barcos_cuatro_celda, "P", matriz)

    # matriz = colocar_barcos_de_cuatro_celdas_vertical(
    #     3, "U", matriz)

    matriz = colocar_barcos_de_tres_celdas_horizontal(
        b3v, "S", matriz)

    matriz = colocar_barcos_de_tres_celdas_vertical(
        b3v, "S", matriz)



    matriz = colocar_barcos_de_dos_celdas_horizontal(
        b2v, "D", matriz)
    matriz = colocar_barcos_de_dos_celdas_vertical(
        (b2v+b2v), "D", matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, "B", matriz)
    return matriz


def obtener_x_aleatoria():
    return random.randint(0, COLUMNAS-1)


def obtener_y_aleatoria():
    return random.randint(0, FILAS-2)


def colocar_barcos_de_una_celda(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        if es_mar(x, y, matriz):
            matriz[y][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def colocar_barcos_de_dos_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and es_mar(x, y, matriz) and es_mar(x2, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def colocar_barcos_de_dos_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and es_mar(x, y, matriz) and es_mar(x, y2, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

# LO QUE MODIFIQUE
def colocar_barcos_de_tres_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y+1
        y3 = y+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and coordenada_en_rango(x, y3) and es_mar(x, y, matriz) and es_mar(x, y2, matriz) and es_mar(x, y3, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            matriz[y3][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_tres_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x+1
        x3 = x+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and coordenada_en_rango(x3, y) and es_mar(x, y, matriz) and es_mar(x2, y, matriz) and es_mar(x3, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            matriz[y][x3] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_cuatro_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x+1
        x3 = x+2
        x4 = x+3
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and coordenada_en_rango(x3, y) and coordenada_en_rango(x4, y) and es_mar(x, y, matriz) and es_mar(x2, y, matriz) and es_mar(x3, y, matriz) and es_mar(x4, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            matriz[y][x3] = tipo_barco
            matriz[y][x4] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_cuatro_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y+1
        y3 = y+2
        y4 = y+3
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and coordenada_en_rango(x, y3) and coordenada_en_rango(x, y4) and es_mar(x, y, matriz) and es_mar(x, y2, matriz) and es_mar(x, y3, matriz) and es_mar(x, y4, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            matriz[y3][x] = tipo_barco
            matriz[y4][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz
# FIN MODDDDDDDD


def imprimir_disparos_restantes(disparos_restantes, jugador):
    print(f"Disparos restantes de {jugador}: {disparos_restantes}")


def imprimir_matriz(matriz, deberia_mostrar_barcos, jugador):
    print(f"Este es el mar del jugador {jugador}: ")
    letra = "A"
    for y in range(FILAS):
        imprimir_separador_horizontal()
        print(f"| {letra} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            valor_real = celda
            if not deberia_mostrar_barcos and valor_real != MAR and valor_real != DISPARO_FALLADO and valor_real != DISPARO_ACERTADO:
                valor_real = " "
            print(f"| {valor_real} ", end="")
        letra = incrementar_letra(letra)
        print("|",)  # Salto de línea
    imprimir_separador_horizontal()
    imprimir_fila_de_numeros()
    imprimir_separador_horizontal()
    # print(matriz)
    # for x in matriz:
    #     print(x)
    #     print("")
    generarGrafo(matriz)


def generarGrafo(matriz):
    print()
    dot = ""
    dot = dot + "\ndigraph G {\n"
    dot = dot + "label=\"Lista de Usuarios\";\n"
    dot = dot + "node [shape=box];\n"

    dot = dot + "//agregar nodos\n"
    letra = "A"
    numero = 1
    numeralL = 1
    contadorColum = 1
    for x in matriz:
        dot = dot + "L" + letra + "[label=\""+ letra + "\"" + ", group = 1" + "];\n"
        for cua in x:
            if cua == "P" or cua == "B" or cua =="S" or cua == "D":
                dot = dot + "U" + str(numeralL) + "[label=\""+ cua + "\"" + ", group = " + str(contadorColum+1) + "];\n"
                numeralL += 1
            contadorColum += 1
        contadorColum = 1
        letra = incrementar_letra(letra)
        
        dot = dot + "N" + str(numero) + "[label=\""+ str(numero) + "\"" + ", group = " + str(numero+1) + "];\n"
        
        numero += 1
    # nodo (0,0)
    dot = dot + "O" + "[label=\""+ "NODO [0,0]" + "\" , group = 1];\n"
    dot = "\n" +dot + "\n"
    dot = dot + "//Enlazar imagenes\n"
    # dot = dot + "{rank=same;\n"
    
    # Conectando Nodos 
    dot = dot + "O->LA" + "\n" + "O->N1" + "\n" 

    letra = "A"
    contador = numero-1
    numero = 1
    numeralL = 1
    #  LETRAS
    for x in matriz:
        dot = dot + "L" + letra 
        # Para no poner una flecha extra
        if contador == (numero):
            dot = dot
        else:
            dot = dot + "->"

        letra = incrementar_letra(letra)
        
        numero += 1
    
    dot = dot + "\n"
    # NUMEROS
    for nu in range(contador):
        nu += 1
        dot = dot + "N" + str(nu)

        if contador == (nu):
            dot = dot
        else:
            dot = dot + "->"

    dot = dot + "\n"

    # NUMEROS MISMO RANGO CON [0,0]
    #  { rank = same; Mt; A0; A1; A2; A3; A4; }
    dot = dot +"{ rank = same; O; "
    contador = numero-1
    numero = 1
    for nu in range(contador):
        nu += 1
        dot = dot + "N" + str(nu)

        if contador == (nu):
            dot = dot
        else:
            dot = dot + "; "
    dot = dot + "}\n"


    # LAS L CON SUS RESPECTIVAS U
    letra = "A"
    numeralL = 1
    for x in matriz:
        dot = dot + "L" + letra 
        
        for cua in x:
            if cua == "P" or cua == "B" or cua =="S" or cua == "D":
                dot = dot + "->" + "U" + str(numeralL)
                numeralL += 1
        letra = incrementar_letra(letra)
    
        dot = dot + "\n"



    dot = dot + "\n"

    #  LA U CON SUS RESPECTIVAS N VERTICAL
    numero = 1
    numeralL = 1
    primeraVez = 0
    matrizNumeroUtilizado = []
    contadorColum = 1
    for x in matriz:
        for cua in x:
            if cua == "P" or cua == "B" or cua =="S" or cua == "D":
                if contadorColum in matrizNumeroUtilizado:
                    dot = dot
                else:
                    dot = dot + "N" + str(contadorColum) + "->"
                
                dot = dot +  "U" + str(numeralL)
                dot = dot + "\n"
                matrizNumeroUtilizado.append(contadorColum)
               
                numeralL += 1

            contadorColum += 1

        
        contadorColum = 1
        primeraVez = 0
        numero += 1
        # dot = dot + "\n"



    # CONECTAR LOS U EN VERTICAL 
    numeralL = 1  
    numero = 1 
    tempMatriz = []
    puta = []
    for x in matriz:
        for cua in x:
            if cua == "P" or cua == "B" or cua =="S" or cua == "D":
                dat = "U"+str(numeralL)
                tempMatriz.append(dat) 
                # print()
                numeralL += 1
            else:
                pato = cua
                tempMatriz.append(pato) 
            
        puta.append(tempMatriz)
        tempMatriz = []
            
    # print(puta)
    for i in range(contador):
        columna = [fila[i] for fila in puta]
        for cua in columna:
            if cua == " ":
                pass
            else:
                dot = dot + cua + "->"
                
        ch = '->'
 
        dot = dot.rstrip(ch)
        dot = dot + "\n"

    dot = dot + "//MISMO RANGO Horiznotal\n"

    letra = "A"
    numeralL = 1
    for x in matriz:
        dot = dot +"{ rank = same; " + "L" + letra + "; "
        for cua in x:
            if cua == "P" or cua == "B" or cua =="S" or cua == "D":
                dot = dot + "U" + str(numeralL) + "; "
                numeralL += 1
        dot = dot + "}\n"
        letra = incrementar_letra(letra)
    
            


    dot = "\n" +dot + "\n"    
    # dot = dot + "\n}\n"
    dot = dot + "}\n"

                
    print(dot)

    # //------->escribir archivo
    # grafo =  Digraph(dot)
    # grafo.edge(dot)
    # print(dot.source)  
    # grafo.render('test-output/graphCiudad.gv', view=True)



root.mainloop()