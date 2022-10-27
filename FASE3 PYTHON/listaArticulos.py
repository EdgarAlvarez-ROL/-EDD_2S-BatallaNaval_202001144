from os import system
class Articulo:
    def __init__(self, nombre, id, categoria, precio, src):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.src = src
        self.categoria = categoria

class Nodo:
    def __init__(self):
        self.elemento = Articulo("","","","","")
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
                print(str(actualNodo.elemento.id) +" "+ (actualNodo.elemento).nombre)
                actualNodo = actualNodo.siguiente
                i+= 1
        else:
            print("LISTA VACIA")
    
    def retornarListaM(self):
        m = []
        actualNodo = Nodo()
        actualNodo = self.Inicio
        i=0
        if (self.Inicio != None):
            while(actualNodo != None):
                # print(str(actualNodo.elemento.id) +" "+ (actualNodo.elemento).nombre)
                m.append(actualNodo.elemento.nombre)
                actualNodo = actualNodo.siguiente
                i+= 1
        else:
            print("LISTA VACIA de ARTICULOS")
        return m

    

    def buscar_Articulo(self,nombre,id):
        actual = Nodo()
        actual = self.Inicio
        encontrado = 0
        nombreUser = nombre
        passw = id
        if (self.Inicio != None):
            while (actual != None and encontrado != 1):
                if (nombreUser == actual.elemento.nombre  and passw == actual.elemento.id):
                    encontrado = 1
                actual = actual.siguiente
        else:
            print("LA LISTA ESTA VACIA")
        
        return encontrado


    def modificar_Articulo(self,nombre,id):
        actual = Nodo()   
        actual = self.Inicio
        i = 0
        if(self.Inicio != None):
            while(actual != None):
                if (nombre == actual.elemento.nombre and id == actual.elemento.id):
                    newnombre = input("Ingrese su nuevo nombre ")
                    newsrc = input("Ingrese su nuevo src ")
                    newPass = input("Ingrese su nuevo id ")
                    actual.elemento.nombre = newnombre
                    actual.elemento.src = newsrc
                    actual.elemento.id = newPass

                    print("LISTO")
                else:
                    i = i+1
                actual = actual.siguiente
        else:
            print("LA LISTA ESTA VACIA")


    def eliminar_Articulo(self,nombre,id):
        actual = Nodo()
        actual = self.Inicio

        anterior = Nodo()
        anterior = None

        encontrado = False

        if (self.Inicio != None):
            while(actual != None and encontrado != True):
                if (nombre == actual.elemento.nombre and id == actual.elemento.id):
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
                        print("Articulo ELIMINADO")
                        encontrado = True
                    elif(confirmacion == "n"):
                        print("Articulo NO elimnado")
                        encontrado = True
                    else:
                        print("Ingrese y o n porfavor")
                        encontrado = True
                anterior = actual
                actual = actual.siguiente
        else:
            print("La lista esta vacia")
        
    def obtenerPreciosTotal(self,item):
        actualNodo = Nodo()
        actualNodo = self.Inicio
        i=0
        precio = 0
        if (self.Inicio != None):
            while(actualNodo != None):
                # print(str(actualNodo.elemento.id) +" "+ (actualNodo.elemento).nombre)
                if actualNodo.elemento.nombre == item:
                    precio = int(actualNodo.elemento.precio)
                actualNodo = actualNodo.siguiente
                i+= 1
        else:
            print("LISTA VACIA")
        return precio


    def grafo_Articulos(self):
        dot = ""
        dot = dot + "\ndigraph G {\n"
        dot = dot + "label=\"Lista de Articulos\";\n"
        dot = dot + "node [shape=box];\n"

        actual = Nodo()
        actual = self.Inicio
        dot = dot +  "//agregar nodos\n"
        if (self.Inicio != None):
            while (actual != None):
                dot = dot + "U" + (actual.elemento.nombre) + "[label=\"" + (actual.elemento.nombre) + "\"];\n"
                actual = actual.siguiente
        
            dot = dot + "//Enlazar imagenes\n"
            dot = dot + "{rank=same;\n"

            #Conectadon nodos de principio a fin
            actual = self.Inicio
            while (actual != None):
                dot = dot + "U" + actual.elemento.nombre
                if (actual.siguiente != None):
                    dot = dot + "->"
                actual = actual.siguiente
            
            dot = "\n" +dot + "\n"

            #Conectadon nodos de fin a principio
            actual = self.Ultimo
            while (actual != None):
                dot = dot + "U" + actual.elemento.nombre
                if (actual.anterior != None):
                    dot = dot + "->"
                actual = actual.anterior

            dot = "\n" +dot + "\n"
            final = Nodo()
            actual = self.Inicio
            final = self.Ultimo

            # Conectando Inicio a Ultimo y Ultimo a Inicio
            dot = dot + "U" + actual.elemento.nombre + "->U" + final.elemento.nombre
            dot = "\n" +dot + "\n"
            dot = dot + "U" + final.elemento.nombre + "->U" + actual.elemento.nombre

        dot = "\n" +dot + "\n"      
        dot = dot + "\n}\n"
        dot = dot + "}\n"

        # print(dot)

        fichero = open("grafos/Articulos.txt", "w")
        fichero.write(dot)
        fichero.close()
        

        system("dot -Tpng -O grafos/Articulos.txt")
        print()



# nuevalista = listaDoble()
# nuevalista.insertar_final(Articulo("ROL","0","asd","33",""))
# nuevalista.insertar_final(Articulo("PEPE","1","asd","423",""))
# nuevalista.insertar_final(Articulo("OSCAR","2","asd","22",""))
# nuevalista.imprimir()

# encontrado = nuevalista.buscar_Articulo("ROL","124")
# print("Encontrado: " + str(encontrado))

# nuevalista.modificar_Articulo("sROL","1234")
# nuevalista.imprimir()

# nuevalista.eliminar_Articulo("ROL","1234")
# nuevalista.imprimir()