/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   ListaCircular.cpp
 * Author: Alex Rose
 * 
 * Created on 6 de agosto de 2022, 09:42 AM
 */
#include "ListaCircular.h"
// #include "PersonaA.h"
// using namespace std;

void ListaCircular::InsertarFinal(PersonaA p1) {
    nodocircu*nuevo = new nodocircu();
    nuevo->p1 = p1;

    if (Inicio == NULL){
        Inicio = nuevo;
        Inicio->sig = NULL;
        Inicio->atras = NULL;
        Ultimo = Inicio;
    }else{
        Ultimo->sig = nuevo;
        nuevo->sig = NULL;
        nuevo->atras = Ultimo;
        Ultimo = nuevo;
    }

}


void ListaCircular::Imprimir() {
    // nodocircu*aux = Inicio;
    nodocircu*actual = new nodocircu();
    actual = Inicio;
    int i;
    i=0;
    if (Inicio != NULL){
        
        while(actual != NULL){
            cout << "\n "<< i << " " << (actual->p1).getNombre();
            actual = actual->sig;
            i = i+1;
        }
        
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}



int ListaCircular::BuscarUsuario(string numberUser, string contrass) {
    nodocircu*actual = new nodocircu();
    actual = Inicio;
    int encontrado = 0;
    string nickUser = numberUser;
    string pass = contrass;
    if (Inicio != NULL){
        
        while(actual != NULL && encontrado != 1){
             if ((nickUser == ((actual->p1).getNombre())) && (pass == ((actual->p1).getPassword())))
            {
                encontrado = 1;
                // cout << encontrado;
            }
            actual = actual->sig;
        }

        // if (encontrado == 0)
        // {
        //     cout <<"Nodo no encontrado";
        // }
        
    }else{
        cout << "La lista esta Vacia";
    }

    return encontrado;
}





void ListaCircular::InsertarEnOrdenReporte(PersonaA p1) {
    nodocircu*nuevo = new nodocircu();
    (nuevo->p1).setEdad(p1.getEdad());
    (nuevo->p1).setMonedas(p1.getMonedas());
    (nuevo->p1).setNombre(p1.getNombre());
    (nuevo->p1).setPassword(p1.getPassword());

    if (Inicio == NULL) {//Si la lista se encuentra vacia
        Inicio = nuevo;
    } else {//si la lista no esta vacia
        nodocircu*auxActual = Inicio;
        nodocircu*auxSiguiente;
        while (auxActual != NULL) {
            auxSiguiente = auxActual->sig;
            if (((nuevo->p1).getEdad()) < ((auxActual->p1).getEdad())) {//insertar al inicio de la lista por que es menor
                nuevo->sig = auxActual;
                Inicio = nuevo;
                break;
            } else if (auxSiguiente == NULL) {//insertar al final de la lista
                auxActual->sig = nuevo;
                break;
            } else if (((nuevo->p1).getEdad()) < ((auxSiguiente->p1).getEdad())) {//insertar en medio de la lista
                auxActual->sig = nuevo;
                nuevo->sig = auxSiguiente;
                break;
            }
            auxActual = auxActual->sig;
        }
    }
}


void ListaCircular::InsertarEnOrdenReporteDESC(PersonaA p1) {
    nodocircu*nuevo = new nodocircu();
    (nuevo->p1).setEdad(p1.getEdad());
    (nuevo->p1).setMonedas(p1.getMonedas());
    (nuevo->p1).setNombre(p1.getNombre());
    (nuevo->p1).setPassword(p1.getPassword());

    if (Inicio == NULL) {//Si la lista se encuentra vacia
        Inicio = nuevo;
    } else {//si la lista no esta vacia
        nodocircu*auxActual = Inicio;
        nodocircu*auxSiguiente;
        while (auxActual != NULL) {
            auxSiguiente = auxActual->sig;
            if (((nuevo->p1).getEdad()) > ((auxActual->p1).getEdad())) {//insertar al inicio de la lista por que es menor
                nuevo->sig = auxActual;
                Inicio = nuevo;
                break;
            } else if (auxSiguiente == NULL) {//insertar al final de la lista
                auxActual->sig = nuevo;
                break;
            } else if (((nuevo->p1).getEdad()) > ((auxSiguiente->p1).getEdad())) {//insertar en medio de la lista
                auxActual->sig = nuevo;
                nuevo->sig = auxSiguiente;
                break;
            }
            auxActual = auxActual->sig;
        }
    }
}









void ListaCircular::ModificarUsuario(string numberUser, string contrass) {
    // nodocircu*aux = Inicio;
    nodocircu*actual = new nodocircu();
    actual = Inicio;
    int i;
    i = 0;
    if (Inicio != NULL){

          while(actual != NULL){
            if (numberUser == ((actual->p1).getNombre()) && contrass == ((actual->p1).getPassword())){
                cout << "\n\nIngrese su nuevo Nick: ";
                string newNick;
                cin >> newNick;
                cout << "Ingrese su nueva Edad: ";
                int newEdad;
                cin >> newEdad;
                cout << "Ingrese su nueva Password: ";
                string newPass;
                cin >> newPass;
                (actual->p1).setNombre(newNick);
                (actual->p1).setEdad(newEdad);
                (actual->p1).setPassword(newPass);

                cout << "Usuario Modificado Exitosamente";
                cout << "\nNombre: " << (actual->p1).getNombre();
                cout << "\nEdad: " << (actual->p1).getEdad();
                cout << "\nPassword: *********** " ;
                
            }
            else{
                i = i+1;
                // cout << "Contrase??a y/o Usuario Incorrecto \n";
            }
            actual = actual->sig;
        }
        
  
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}



void ListaCircular::EliminarUsuario(string numberUser, string contrass) {
    // nodocircu*aux = Inicio;
    nodocircu*actual = new nodocircu();
    actual = Inicio;

    nodocircu*anterior = new nodocircu();
    anterior = NULL;

    int i;
    i = 0;

    bool encontrado = false;
    if (Inicio != NULL){

          while(actual != NULL && encontrado!=true){

            if (numberUser == ((actual->p1).getNombre()) && contrass == ((actual->p1).getPassword())){
                // cout << "Usuario Encontrado\n";
                cout << "\nDESEA ELIMINAR SU CUENTA [y/n]: ";
                string confirmacion;
                cin >> confirmacion;
                if (confirmacion == "y"){
                      if (actual == Inicio){
                        Inicio = Inicio->sig;
                        Inicio->atras = NULL;
                    }else if (actual == Ultimo){
                        anterior->sig = NULL;
                        Ultimo = anterior;
                    }else{
                        anterior->sig = actual->sig;
                        actual->sig->atras = anterior;
                    }

                    cout << "\n Usuario Eliminado \n";
                    encontrado = true;
                }else if (confirmacion == "n"){
                    cout << "\n Usuario NO Eliminado \n";
                    encontrado = true;
                }else{
                    cout << "\nIngrese [y/n] porfavor";
                    encontrado = true;
                }
                
                  
                    // encontrado = true;
            }
            else{
                i = i+1;
                // cout << "Contrase??a y/o Usuario Incorrecto \n";
            }
            anterior = actual;
            actual = actual->sig;
        }
        
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}

void ListaCircular::GrafoASCUsuarios() {
    string dot = "";
    dot = dot + "\ndigraph G {\n";
    dot = dot + "label=\"Lista de Usuarios\";\n";
    dot = dot + "node [shape=box];\n";

    nodocircu*actual = Inicio;
    dot = dot + "//agregar nodos\n";

    while (actual != NULL) {
        // cout <<"[" << (aux->p1).getEdad() << "]->";
        dot = dot + "U" + ((actual->p1).getNombre()) + "[label=\"" + " Nombre: " + (actual->p1).getNombre() + " \nEdad:" + std::to_string((actual->p1).getEdad()) + "\"];\n";
        actual = actual->sig;
    }
    
    dot = dot + "//Enlazar imagenes\n";
    dot = dot + "{rank=same;\n";
    /**CONECTANDO NODOS DE PRINCIPIO A FIN**/
    actual = Inicio;
    while (actual != NULL) {
        dot = dot + "U" + ((actual->p1).getNombre());
        if (actual->sig != NULL) {
            dot = dot + "->";
        }
    actual = actual->sig;
    }
    dot = "\n" +dot + "\n";     
    dot = dot + "\n}\n";
    dot = dot + "}\n";

    cout << dot;

    //------->escribir archivo
    ofstream file;
    file.open("UsuarioOrdenAsc.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng UsuarioOrdenAsc.dot -o  UsuarioOrdenAsc.png"));

    //------>abrir archivo
    system(("UsuarioOrdenAsc.png"));
    


}


void ListaCircular::GrafoUsuarios() {
    string dot = "";
    dot = dot + "\ndigraph G {\n";
    dot = dot + "label=\"Lista de Usuarios\";\n";
    dot = dot + "node [shape=box];\n";

    nodocircu*actual = new nodocircu();
    actual = Inicio;
    dot = dot + "//agregar nodos\n";
    // int i;
    // i=0;
    if (Inicio != NULL){
        
        while(actual != NULL){
            dot = dot + "U" + ((actual->p1).getNombre()) + "[label=\"" + (actual->p1).getNombre() + "\"];\n";
            // cout << "\n "<< i << " " << (actual->p1).getNombre();
            actual = actual->sig;
            // i = i+1;
        }

        dot = dot + "//Enlazar imagenes\n";
        dot = dot + "{rank=same;\n";

        /**CONECTANDO NODOS DE PRINCIPIO A FIN**/
        actual = Inicio;
        while (actual != NULL) {
        dot = dot + "U" + ((actual->p1).getNombre());
        if (actual->sig != NULL) {
            dot = dot + "->";
        }
        actual = actual->sig;
        }

        dot = "\n" +dot + "\n"; 

        /**CONECTANDO NODOS DE fIN A PRINCIPIO**/
        actual = Ultimo;
        while (actual != NULL) {
        dot = dot + "U" + ((actual->p1).getNombre());
        if (actual->atras != NULL) {
            dot = dot + "->";
        }
        actual = actual->atras;
        }

         dot = "\n" +dot + "\n";  

        nodocircu*final = new nodocircu();
        actual = Inicio;
        final = Ultimo;

        dot = dot + "U" + ((actual->p1).getNombre()) + "->U" + ((final->p1).getNombre());
        dot = "\n" +dot + "\n"; 
        dot = dot + "U" + ((final->p1).getNombre()) + "->U" + ((actual->p1).getNombre());


    dot = "\n" +dot + "\n";        
    dot = dot + "\n}\n";
    dot = dot + "}\n";

    cout << dot;

    //------->escribir archivo
    ofstream file;
    file.open("Usuarios.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng Usuarios.dot -o  Usuarios.png"));

    //------>abrir archivo
    system(("Usuarios.png"));
    
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}



