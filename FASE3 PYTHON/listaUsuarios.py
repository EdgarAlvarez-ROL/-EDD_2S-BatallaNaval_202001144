from mmap import ACCESS_COPY, ALLOCATIONGRANULARITY
from os import system
from xml.dom.minidom import Element
from graphviz import Digraph

class Usuario:
    def __init__(self, nick, password, monedas, edad):
        self.nick = nick
        self.password = password
        self.monedas = monedas
        self.edad = edad

class Nodo:
    def __init__(self):
        self.elemento = Usuario("","","","")
        self.siguiente = None
        self.anterior = None

class listaDoble:
    def __init__(self):
        self.Inicio = None
        self.Ultimo = None

    
    
    def insertar_final(self, dato):
        nuevoNodo = Nodo()
        nuevoNodo.elemento = dato

        if (self.Inicio == None):
            self.Inicio = nuevoNodo
            self.Inicio.siguiente = None
            self.Inicio.anterior = None
            self.Ultimo = self.Inicio
        else:
            self.Ultimo.siguiente = nuevoNodo
            nuevoNodo.siguiente = None
            nuevoNodo.anterior = self.Ultimo
            self.Ultimo = nuevoNodo

       

    def imprimir(self):
        actualNodo = Nodo()
        actualNodo = self.Inicio
        i=0
        if (self.Inicio != None):
            while(actualNodo != None):
                print(str(i) +" "+ (actualNodo.elemento).nick)
                actualNodo = actualNodo.siguiente
                i+= 1
        else:
            print("LISTA VACIA")
    

    def buscar_usuario(self,nick,password):
        actual = Nodo()
        actual = self.Inicio
        encontrado = 0
        nickUser = nick
        passw = password
        if (self.Inicio != None):
            while (actual != None and encontrado != 1):
                if (nickUser == actual.elemento.nick  and passw == actual.elemento.password):
                    encontrado = 1
                actual = actual.siguiente
        else:
            print("LA LISTA ESTA VACIA")
        
        return encontrado


    def modificar_usuario(self,nick,password):
        actual = Nodo()   
        actual = self.Inicio
        i = 0
        if(self.Inicio != None):
            while(actual != None):
                if (nick == actual.elemento.nick and password == actual.elemento.password):
                    newNick = input("Ingrese su nuevo Nick ")
                    newEdad = input("Ingrese su nuevo Edad ")
                    newPass = input("Ingrese su nuevo Password ")
                    actual.elemento.nick = newNick
                    actual.elemento.edad = newEdad
                    actual.elemento.password = newPass

                    print("LISTO")
                else:
                    i = i+1
                actual = actual.siguiente
        else:
            print("LA LISTA ESTA VACIA")


    def eliminar_usuario(self,nick,password):
        actual = Nodo()
        actual = self.Inicio

        anterior = Nodo()
        anterior = None

        encontrado = False

        if (self.Inicio != None):
            while(actual != None and encontrado != True):
                if (nick == actual.elemento.nick and password == actual.elemento.password):
                    confirmacion = input("DESEA ELIMINAR SU CUENTA [y/n]: ")
                    if (confirmacion == "y"):
                        if (actual == self.Inicio):
                            self.Inicio = self.Inicio.siguiente
                            self.Inicio.anterior = None
                        elif (actual == self.Ultimo):
                            self.Ultimo.siguiente = None
                            self.Ultimo = anterior
                        else:
                            anterior.siguiente = actual.siguiente
                            actual.siguiente.anterior  = anterior
                        print("USUARIO ELIMINADO")
                        encontrado = True
                    elif(confirmacion == "n"):
                        print("Usuario NO elimnado")
                        encontrado = True
                    else:
                        print("Ingrese y o n porfavor")
                        encontrado = True
                anterior = actual
                actual = actual.siguiente
        else:
            print("La lista esta vacia")


    def grafo_usuarios(self):
        dot = ""
        dot = dot + "\ndigraph G {\n"
        dot = dot + "label=\"Lista de Usuarios\";\n"
        dot = dot + "node [shape=box];\n"

        actual = Nodo()
        actual = self.Inicio
        dot = dot +  "//agregar nodos\n"
        if (self.Inicio != None):
            while (actual != None):
                dot = dot + "U" + (actual.elemento.nick) + "[label=\"" + (actual.elemento.nick) + "\"];\n"
                actual = actual.siguiente
        
            dot = dot + "//Enlazar imagenes\n"
            dot = dot + "{rank=same;\n"

            #Conectadon nodos de principio a fin
            actual = self.Inicio
            while (actual != None):
                dot = dot + "U" + actual.elemento.nick
                if (actual.siguiente != None):
                    dot = dot + "->"
                actual = actual.siguiente
            
            dot = "\n" +dot + "\n"

            #Conectadon nodos de fin a principio
            actual = self.Ultimo
            while (actual != None):
                dot = dot + "U" + actual.elemento.nick
                if (actual.anterior != None):
                    dot = dot + "->"
                actual = actual.anterior

            dot = "\n" +dot + "\n"
            final = Nodo()
            actual = self.Inicio
            final = self.Ultimo

            # Conectando Inicio a Ultimo y Ultimo a Inicio
            dot = dot + "U" + actual.elemento.nick + "->U" + final.elemento.nick
            dot = "\n" +dot + "\n"
            dot = dot + "U" + final.elemento.nick + "->U" + actual.elemento.nick

        dot = "\n" +dot + "\n"      
        dot = dot + "\n}\n"
        dot = dot + "}\n"

        # print(dot)

        fichero = open("grafos/usuarios.txt", "w")
        fichero.write(dot)
        fichero.close()
        

        system("dot -Tpng -O grafos/usuarios.txt")
        print()


# nuevalista = listaDoble()
# nuevalista.insertar_final(Usuario("ROL","1234","44","21"))
# nuevalista.insertar_final(Usuario("PEPE","SAFD","ASDF","ASDF"))
# nuevalista.insertar_final(Usuario("OSCAR","12","12","22"))
# nuevalista.imprimir()

# encontrado = nuevalista.buscar_usuario("ROL","124")
# print("Encontrado: " + str(encontrado))

# nuevalista.modificar_usuario("sROL","1234")
# nuevalista.imprimir()

# nuevalista.eliminar_usuario("ROL","1234")
# nuevalista.imprimir()

# nuevalista.grafo_usuarios()

