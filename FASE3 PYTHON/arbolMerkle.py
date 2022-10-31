class Nodo:
   def __init__(self, dato):
      # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
      self.dato = dato
      self.izquierda = None
      self.derecha = None


class Arbol:
   # Funciones privadas
   def __init__(self, dato):
       self.raiz = Nodo(dato)

   def __agregar_recursivo(self, nodo, dato):
      if dato < nodo.dato:
           if nodo.izquierda is None:
               nodo.izquierda = Nodo(dato)
               # nodo.derecha = Nodo("-1")
           else:
               self.__agregar_recursivo(nodo.izquierda, dato)
      else:
           if nodo.derecha is None:
               nodo.derecha = Nodo(dato)
         #   elif nodo.derecha == "-1":
         #       nodo.derecha = Nodo(dato)
           else:
               self.__agregar_recursivo(nodo.derecha, dato)

   def __inorden_recursivo(self, nodo):
      if nodo is not None:
           self.__inorden_recursivo(nodo.izquierda)
           print(nodo.dato, end=", ")
           self.__inorden_recursivo(nodo.derecha)

   def __preorden_recursivo(self, nodo):
      if nodo is not None:
           print(nodo.dato, end=", ")
           self.__preorden_recursivo(nodo.izquierda)
           self.__preorden_recursivo(nodo.derecha)

   def __postorden_recursivo(self, nodo):
      if nodo is not None:
           self.__postorden_recursivo(nodo.izquierda)
           self.__postorden_recursivo(nodo.derecha)
           print(nodo.dato, end=", ")

   def __buscar(self, nodo, busqueda):
      if nodo is None:
          return None
      if nodo.dato == busqueda:
          return nodo
      if busqueda < nodo.dato:
          return self.__buscar(nodo.izquierda, busqueda)
      else:
          return self.__buscar(nodo.derecha, busqueda)

   # Funciones públicas
   def agregar(self, dato):
      counter = self.contarMomentum()
      # print(counter)
      if counter == 2:
         with open("momentum.txt") as archivo:
            for linea in archivo:
               print(linea)
               self.__agregar_recursivo(self.raiz, linea.rstrip())
         
         archivo.close()
         archivo= open("momentum.txt","w")
         archivo.write(dato+"\n")
         archivo.close() #Cierras el archivo.
                     
      else:
         archivo = open("momentum.txt","a")
         archivo.write(dato+"\n")
         archivo.close()

   def inorden(self):
      print("Imprimiendo árbol inorden: ")
      self.__inorden_recursivo(self.raiz)
      print("")

   def preorden(self):
      print("Imprimiendo árbol preorden: ")
      self.__preorden_recursivo(self.raiz)
      print("")

   def postorden(self):
      print("Imprimiendo árbol postorden: ")
      self.__postorden_recursivo(self.raiz)
      print("")

   def buscar(self, busqueda):
      return self.__buscar(self.raiz, busqueda)

   def contarMomentum(self):
      file = open("momentum.txt","r") 
      Counter = 0
      
      Content = file.read() 
      CoList = Content.split("\n") 
      
      for i in CoList: 
         if i: 
            Counter += 1
               
      # print("This is the number of lines in the file") 
      # print(Counter) 
      return Counter

   



# arbol = Arbol("Luis")
# arbol.agregar("Maria Jose")
# arbol.agregar("Leon")
# arbol.agregar("Cuphead")
# arbol.agregar("Maggie")

# arbol.preorden()

