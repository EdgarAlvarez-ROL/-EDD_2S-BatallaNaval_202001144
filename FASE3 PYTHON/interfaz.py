from ast import Pass, Str
from importlib.metadata import entry_points
from logging import root
from multiprocessing import BufferTooShort
from operator import ge
from pickle import GLOBAL
from mmap import ACCESS_COPY, ALLOCATIONGRANULARITY
from os import system
import tkinter
# import imgkit
from sre_parse import State
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox, ttk, PhotoImage
from tkinter import messagebox as MessageBox

from tkinter.ttk import *

import random
import os
from graphviz import Digraph, Graph

#Otros archivos de la carpeta
from lectorJson import *

#LISTAS
import listaUsuarios
lista_de_usuarios = listaUsuarios.listaDoble()


#MATRIZ DISPERSA VARIABLES GLOBALES 
FILAS = 10
COLUMNAS = 10
MAR = " "
SUBMARINO = "S"  # Ocupa una celda
DESTRUCTOR = "D"  # Ocupa dos celdas
PRUEBA = "P"
DESTRUCTOR_VERTICAL = "A"  # Ocupa dos celdas
DISPARO_FALLADO = "X" #ESTE ERA MENOS "-"
DISPARO_ACERTADO = "X"
DISPAROS_INICIALES = 2
CANTIDAD_BARCOS_INICIALES = 1
JUGADOR_1 = "J1"
JUGADOR_2 = "J2"



#Variables Globales
nick = ""
password = ""

barcos_una_celda = 0
barcos_dos_celda = 0
barcos_tres_celda = 0
barcos_cuatro_celda = 0


# Nombre de la ventana
root = Tk(className='Ventana de ejemplo')

# Ver las imagenes
photo3 = PhotoImage(file = "grafos/matrizDispersa1.txt.png") 
photo_subsambple = photo3.subsample(3,3)

photo = PhotoImage(file = "grafos/matrizDispersa2.txt.png") 
photo_subsambple2 = photo.subsample(3,3)

matriz_j1 = []
matriz_j2 = []
turno_actual = "J1"

# Funciones para los Botones
def pagv_juego():
    global matriz_j1, matriz_j2, turno_actual
    # global photo3, photo_subsambple, photo, photo_subsambple2
    v_juego = Toplevel()
    v_juego.geometry("1000x600")
    v_juego.title("v_juego")
    # v_juego.attributes('-toolwindow', True)  #QUITAR MAXIMIZAR Y MINIMIZAR
    # v_juego.resizable(0,0)  #BLOQUEAR EL MAXIMIZAR Y MINIMIZAR

    
    def nCuadricula(): 
        global matriz_j1, matriz_j2
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
            
            matriz_j1, matriz_j2 = obtener_matriz_inicial(), obtener_matriz_inicial()
            matriz_j1 = colocar_e_imprimir_barcos(matriz_j1, cantidad_barcos, JUGADOR_1)
            matriz_j2 = colocar_e_imprimir_barcos(matriz_j2, cantidad_barcos, JUGADOR_2)

            generarGrafo(matriz_j1,JUGADOR_1)
            generarGrafo(matriz_j2,JUGADOR_2)


            photo = PhotoImage(file = "grafos/matrizDispersa1.txt.png")
            photo_subsambple = photo.subsample(3,3) 
            lbl_img.configure(image=photo_subsambple)
            lbl_img.image=photo_subsambple

            photo = PhotoImage(file = "grafos/matrizDispersa2.txt.png") 
            photo_subsambple2 = photo.subsample(3,3)
            lbl_img2.configure(image=photo_subsambple2)
            lbl_img2.image=photo_subsambple2
            MessageBox.showinfo("GANADOR", "EL JUGADOR 2 ES EL JUGADOR INVITADO") # título, mensaje
        elif (m<= 20 and m>10):
            etiqueta['text'] = "Bien"
            nPortaaviones = 2
            nSubmarinos = 4
            nDestructores = 6
            nBuques = 8

            cantidad_barcos = nPortaaviones + nSubmarinos + nDestructores + nBuques
            configurar_cantidad_barcos(nBuques, nDestructores, nSubmarinos, nPortaaviones, cantidad_barcos, m)
            
            matriz_j1, matriz_j2 = obtener_matriz_inicial(), obtener_matriz_inicial()
            matriz_j1 = colocar_e_imprimir_barcos(matriz_j1, cantidad_barcos, JUGADOR_1)
            matriz_j2 = colocar_e_imprimir_barcos(matriz_j2, cantidad_barcos, JUGADOR_2)

            generarGrafo(matriz_j1, JUGADOR_1)
            generarGrafo(matriz_j2, JUGADOR_2)

            photo = PhotoImage(file = "grafos/matrizDispersa1.txt.png")
            photo_subsambple = photo.subsample(3,3) 
            lbl_img.configure(image=photo_subsambple)
            lbl_img.image=photo_subsambple

            photo = PhotoImage(file = "grafos/matrizDispersa2.txt.png") 
            photo_subsambple2 = photo.subsample(3,3)
            lbl_img2.configure(image=photo_subsambple2)
            lbl_img2.image=photo_subsambple2

            MessageBox.showinfo("GANADOR", "EL JUGADOR 2 ES EL JUGADOR INVITADO") # título, mensaje
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
            
            matriz_j1, matriz_j2 = obtener_matriz_inicial(), obtener_matriz_inicial()
            matriz_j1 = colocar_e_imprimir_barcos(matriz_j1, cantidad_barcos, JUGADOR_1)
            matriz_j2 = colocar_e_imprimir_barcos(matriz_j2, cantidad_barcos, JUGADOR_2)

            generarGrafo(matriz_j1, JUGADOR_1)
            generarGrafo(matriz_j2, JUGADOR_2)
        
            photo = PhotoImage(file = "grafos/matrizDispersa1.txt.png")
            photo_subsambple = photo.subsample(4,4) 
            lbl_img.configure(image=photo_subsambple)
            lbl_img.image=photo_subsambple

            photo = PhotoImage(file = "grafos/matrizDispersa2.txt.png") 
            photo_subsambple2 = photo.subsample(4,4)
            lbl_img2.configure(image=photo_subsambple2)
            lbl_img2.image=photo_subsambple2
        # print(matriz1temp)
           
    def regresarPagPrincipal():
        v_juego.destroy()
        root.deiconify()


    def todos_los_barcos_hundidos(matriz):
        for y in range(FILAS):
            for x in range(COLUMNAS):
                celda = matriz[y][x]
                # Si no es mar o un disparo, significa que todavía hay un barco por ahí
                if celda != MAR and celda != DISPARO_ACERTADO and celda != DISPARO_FALLADO:
                    return False
        # Acabamos de recorrer toda la matriz y no regresamos en la línea anterior. Entonces todos los barcos han sido hundidos
        return True


    def solicitar_coordenadas(jugador):
        # print(f"Solicitando coordenadas de disparo al jugador {jugador}")
        # Ciclo infinito. Se rompe cuando ingresan una fila correcta
        y = None
        x = None
        while True:
            letra_fila = coordenada_letra.get()
            # Necesitamos una letra de 1 carácter. Si no es de 1 carácter usamos continue para repetir este ciclo
            if len(letra_fila) != 1:
                print("Debes ingresar únicamente una letra")
                continue
            # Convertir la letra a un índice para acceder a la matriz
            # La A equivale al ASCII 65, la B al 66, etcétera. Para convertir la letra a índice
            # convertimos la letra a su ASCII y le restamos 65 (el 65 es el ASCII de la A, por lo que A es 0)
            y = ord(letra_fila) - 65
            # Verificar si es válida. En caso de que sí, rompemos el ciclo
            if coordenada_en_rango(0, y):
                break
            else:
                print("Fila inválida")
                x = 99
                break
        # Hacemos lo mismo pero para la columna
        while True:
            try:
                x = int(coordenada_numero.get())
                if coordenada_en_rango(x-1, 0):
                    x = x-1  # Queremos el índice, así que restamos un 1 siempre
                    break
                else:
                    print("Columna inválida")
                    x = 99
                    break
            except:
                print("Ingresa un número válido")

        return x, y

    def disparar(x, y, matriz) -> bool:
        if es_mar(x, y, matriz):
            matriz[y][x] = DISPARO_FALLADO
            pass
            return False
        # Si ya había disparado antes, se le cuenta como falla igualmente
        elif matriz[y][x] == DISPARO_FALLADO or matriz[y][x] == DISPARO_ACERTADO:
            return False
        else:
            matriz[y][x] = DISPARO_ACERTADO
            return True


    def iniciar_disparos():
        global turno_actual
        if turno_actual == JUGADOR_2:
            x, y = solicitar_coordenadas(turno_actual)
            acertado = disparar(x, y, matriz_j1)
            if acertado:
                if todos_los_barcos_hundidos(matriz_j1):
                    MessageBox.showinfo("GANADOR", "EL JUGADOR 2 GANO") # título, mensaje
                # grafoAdyacencia(matriz_j1,JUGADOR_2)
            print(acertado)

            generarGrafo(matriz_j1,JUGADOR_1)
            photo = PhotoImage(file = "grafos/matrizDispersa1.txt.png") 
            photo_subsambple = photo.subsample(3,3)
            lbl_img.configure(image=photo_subsambple)
            lbl_img.image=photo_subsambple
            
            turno_actual = JUGADOR_1
            turno_jugadpr['text'] = "TURNO DEL JUGADOR 1"
        else:
            x, y = solicitar_coordenadas(turno_actual)
            acertado = disparar(x, y, matriz_j2)
            print(acertado)
            if acertado:
                if todos_los_barcos_hundidos(matriz_j1):
                    MessageBox.showinfo("GANADOR", "EL JUGADOR 1 GANO") # título, mensaje
                grafoAdyacencia(matriz_j2,JUGADOR_1)

            generarGrafo(matriz_j2,JUGADOR_2)
            photo = PhotoImage(file = "grafos/matrizDispersa2.txt.png") 
            photo_subsambple2 = photo.subsample(3,3)
            lbl_img2.configure(image=photo_subsambple2)
            lbl_img2.image=photo_subsambple2
            
            turno_actual = JUGADOR_2
            turno_jugadpr['text'] = "TURNO DEL JUGADOR 2"
        # imprimir_matriz(matriz_j1,True,JUGADOR_1)
        
        print()
    
    
    
    #Etiquetas 
    Label(v_juego, text="Ingrese el valor de la dimension del tablero").place(x=10, y=75)
    etiqueta = ttk.Label(v_juego, text="")
    etiqueta.place(x=10, y=320)
    
    #Caja de Texso
    caja1 = ttk.Entry(v_juego)
    caja1.place(x=10, y=100)
    caja1.insert(0,"10")
    
    #Botones
    Button(v_juego, text="Crear Tablero", command=nCuadricula).place(x=10,y=200)
   
    lbl_img = ttk.Label(v_juego, image=photo_subsambple)
    lbl_img.place(x=300, y=5)

    lbl_img2 = ttk.Label(v_juego, image=photo_subsambple2)
    lbl_img2.place(x=800, y=5)

    #ENTRYS CAJAS DE TEXTO \n
    # entry_campo1 = ttk.Label(v_juego, text ="")
    # entry_campo1.place(x=300, y=5, width=400, height=400)
    # entry_campo1['text'] = "asfasdfasdflajsd\nfadfsasdfasdfasf"
    
    
    
    # BOTONES Y COSAS PARA DISPARAR
    turno_jugadpr = ttk.Label(v_juego, text="TURNO DEL JUGADOR 1")
    turno_jugadpr.place(x=10, y=280)
    
    Label(v_juego, text="Ingrese la Letra: ").place(x=10, y=300)
    coordenada_letra = ttk.Entry(v_juego)
    coordenada_letra.place(x=120, y=300)

    Label(v_juego, text="Ingrese el Numero: ").place(x=10, y=350)
    coordenada_numero = ttk.Entry(v_juego)
    coordenada_numero.place(x=120, y=350)

    Button(v_juego, text="DISPARAR",command=iniciar_disparos).place(x=10,y=420)



    v_juego.protocol("WM_DELETE_WINDOW", regresarPagPrincipal) #CERRAR PESTAÑA Y REGRESAR AL INICIO
    
    



def pagAdmin():
    v_admiin = Tk(className='admin')
    v_admiin.geometry("600x400")
    v_admiin.resizable (0,0) #Evitar que los usuarios ajusten el tamaño.

    #Botones
    def v_a_leerJson():
        filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.json*"), 
                                                       ("all files", 
                                                        "*.*")))
        print(filename)
        usuarios = leerJson(filename)
        for i in (usuarios["usuarios"]):
            # insertar_final(Usuario("ROL","1234","44","21"))
            usuarioA = listaUsuarios.Usuario("","","","")
            usuarioA.nick = i["nick"]
            usuarioA.password = i["password"]
            usuarioA.monedas = i["monedas"]
            usuarioA.edad = i["edad"]
            lista_de_usuarios.insertar_final(usuarioA)

        # lista_de_usuarios.imprimir()
        lista_de_usuarios.grafo_usuarios()
    
    def regresar_al_inicio():
        v_admiin.destroy()
        root.deiconify()
        # iniciarTodo()
        

    Button(v_admiin, text="Ver objetos en el sistema").place(x=50,y=50)
    Button(v_admiin, text="Ver usuarios en el sistema").place(x=50,y=200)
    Button(v_admiin, text="leer JSON",command=v_a_leerJson).place(x=50,y=320)
    Button(v_admiin, text="REGRESAR",command=regresar_al_inicio).place(x=220,y=20)

   

def iniciarTodo():
    

    #dando el tamaño a la ventana
    root.geometry("500x400")
    root.resizable (0,0) #Evitar que los usuarios ajusten el tamaño.

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



    def Ingresar():
        nick = caja1.get()
        password =  caja2.get()
        # print(password)
        # print(nick)

        if ((nick.strip()) == "EDD" and (password.strip()) == "edd123"):
            #Iniciando la seccion del ADMIN
            pagAdmin()

            #Cerrando la Ventana de LOGIN
            root.withdraw()
        elif lista_de_usuarios.buscar_usuario(nick.strip(),password.strip()):
            # print()
            JUGADOR_1 = nick.strip()
            pagv_juego()
            #Cerrando la Ventana de LOGIN
            root.withdraw()
        elif (nick.strip() == "1" and password.strip() == "1"):
            # print()
            pagv_juego()
            #Cerrando la Ventana de LOGIN
            root.withdraw()
        else:
            print("contraseña o usuario incorrecto")
        # root.destroy()

    #Botones
    Button(root, text="INGRESAR", command=Ingresar).place(x=200,y=300)


    root.mainloop()


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
    # global campo1TEXT
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
    # print(CANTIDAD_BARCOS_INICIALES)

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





def generarGrafo(matriz, jugador):
    print()
    dot = ""
    dot = dot + "\ndigraph G {\n"
    dot = dot + "label=\"Campo de " + jugador + "\";\n"
    dot = dot + "node [shape=box, style=filled, fontsize=\"30pt\", fontname=\"Arial\"];\n"

    dot = dot + "//agregar nodos\n"
    letra = "A"
    numero = 1
    numeralL = 1
    contadorColum = 1
    for x in matriz:
        dot = dot + "L" + letra + "[label=\""+ letra + "\"" + ", group = 1" + "];\n"
        for cua in x:
            if cua == "P":
                dot = dot + "U" + str(numeralL) + "[label=\""+ cua + "\"" + ", group = " + str(contadorColum+1) + ", fillcolor=green];\n"
                numeralL += 1
            elif cua == "B":
                dot = dot + "U" + str(numeralL) + "[label=\""+ cua + "\"" + ", group = " + str(contadorColum+1) + ", fillcolor=yellow];\n"
                numeralL += 1
            elif cua =="S":
                dot = dot + "U" + str(numeralL) + "[label=\""+ cua + "\"" + ", group = " + str(contadorColum+1) + ", fillcolor=pink];\n"
                numeralL += 1 
            elif cua == "D":
                dot = dot + "U" + str(numeralL) + "[label=\""+ cua + "\"" + ", group = " + str(contadorColum+1) + ", fillcolor=orange];\n"
                numeralL += 1 
            elif cua == "X":
                dot = dot + "U" + str(numeralL) + "[label=\""+ cua + "\"" + ", group = " + str(contadorColum+1) + ", fillcolor=black];\n"
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
            if cua == "P" or cua == "B" or cua =="S" or cua == "D" or cua == "X":
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
            if cua == "P" or cua == "B" or cua =="S" or cua == "D" or cua == "X":
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
            if cua == "P" or cua == "B" or cua =="S" or cua == "D" or cua == "X":
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
            if cua == "P" or cua == "B" or cua =="S" or cua == "D" or cua == "X":
                dot = dot + "U" + str(numeralL) + "; "
                numeralL += 1
        dot = dot + "}\n"
        letra = incrementar_letra(letra)
    
            


    dot = "\n" +dot + "\n"    
    # dot = dot + "\n}\n"
    dot = dot + "}\n"

    #Imprimir los datos para generar la matriz inversa
    # print(dot)

    if jugador != JUGADOR_2:
        fichero = open("grafos/matrizDispersa1.txt","w")
        fichero.write(dot)
        fichero.close()
        
        system("dot -Tpng -O grafos/matrizDispersa1.txt")
        print()
    else:
        fichero = open("grafos/matrizDispersa2.txt","w")
        fichero.write(dot)
        fichero.close()
        
        system("dot -Tpng -O grafos/matrizDispersa2.txt")
        print()

   

    # //------->escribir archivo
    # grafo =  Digraph(dot)
    # grafo.edge(dot)
    # print(dot.source)  
    # grafo.render('test-output/graphCiudad.gv', view=True)


def grafoAdyacencia(matriz, jugador):
    dot = ""
    dot = dot + "\ndigraph G {\n"
    dot = dot + "label=\"Campo de " + jugador + "\";\n"
    dot = dot + "node [shape=box, style=filled, fontsize=\"30pt\", fontname=\"Arial\"];\n"

    dot = dot + "//agregar nodos\n"
    letra = "A"
    contador = 1
    numeroNodo = 1
    listaGeneral = []
    minilista = []
    for y in matriz:
        dot = dot + "L" + letra + "[label=\""+ letra + "\"" + "" + "];\n"
        minilista.append(("L"+letra))
        for x in y:
            if x =="X":
                dot = dot + "N" + str(contador) + "[label=\""+ str(contador) + "\"" + "" + "];\n"
                numeroNodo += 1
                minilista.append("N"+(str(contador)))
            contador += 1
        contador = 1
        letra = incrementar_letra(letra)
        listaGeneral.append(minilista)
        minilista = []
        
    dot = dot + "\n" 
    # print(listaGeneral)
    for y in listaGeneral:
        for x in y:
            dot = dot + x 
            if y[-1] == x:
                pass
            else: 
                dot = dot + "->"
        dot = dot + "\n" 
    
    dot = "\n" +dot + "\n"  
    dot = dot + "}\n"
    print(dot)
    
    
    print()



iniciarTodo()