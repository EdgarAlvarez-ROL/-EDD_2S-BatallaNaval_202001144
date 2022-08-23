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
        
        
        /*Lista Doble Simple*/
        // do{
        //     cout << "\n "<< i << " " << (actual->p1).getNombre();
        //     actual = actual->sig;
        //     i = i + 1;
        // }while(actual != Inicio);
    }else{
        cout << "LA LISTA ESTA VACIA";
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
                // cout << "Contraseña y/o Usuario Incorrecto \n";
            }
            actual = actual->sig;
        }
        

        // do{
        //     // cout << "\n " << (actual->p1).getNombre();
        //     if (numberUser == i && contrass == ((actual->p1).getPassword())){
        //         cout << "\n\nIngrese su nuevo Nick: ";
        //         string newNick;
        //         cin >> newNick;
        //         cout << "Ingrese su nueva Edad: ";
        //         int newEdad;
        //         cin >> newEdad;
        //         cout << "Ingrese su nueva Password: ";
        //         string newPass;
        //         cin >> newPass;
        //         (actual->p1).setNombre(newNick);
        //         (actual->p1).setEdad(newEdad);
        //         (actual->p1).setPassword(newPass);

        //         cout << "Usuario Modificado Exitosamente";
        //         cout << "Nombre: " << (actual->p1).getNombre();
        //         cout << "Edad: " << (actual->p1).getEdad();
        //         cout << "Password: ****** " ;
                
        //     }
        //     else{
        //         i = i+1;
        //         // cout << "Contraseña y/o Usuario Incorrecto \n";
        //     }
        //     actual = actual->sig;
            
        // }while(actual != Inicio);
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
                cout << "Usuario Encontrado\n";
                cout << "DESEA ELIMINAR SU CUENTA [y/n]: ";
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
                // cout << "Contraseña y/o Usuario Incorrecto \n";
            }
            anterior = actual;
            actual = actual->sig;
        }
        
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
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





int ListaCircular::BuscarUsuario(string numberUser, string contrass) {
    nodocircu*actual = new nodocircu();
    actual = Inicio;

    bool encontrado = false;
    int monedas;

    while(actual != NULL && encontrado!=true){

        if (numberUser == ((actual->p1).getNombre()) && contrass == ((actual->p1).getPassword())){
                // cout << "Usuario Encontrado\n";
                encontrado = true;
                monedas = ((actual->p1).getMonedas());
        }
        // anterior = actual;
        actual = actual->sig;
    }

    return encontrado, monedas;
 
}
