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

    if(Inicio == NULL){
        Inicio = nuevo;
        Inicio->sig = Inicio;
        Ultimo  = Inicio;
    }else{
        Ultimo->sig = nuevo;
        nuevo->sig = Inicio;
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
        do{
            cout << "\n "<< i << " " << (actual->p1).getNombre();
            actual = actual->sig;
            i = i + 1;
        }while(actual != Inicio);
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}


void ListaCircular::ModificarUsuario(int numberUser, string contrass) {
    // nodocircu*aux = Inicio;
    nodocircu*actual = new nodocircu();
    actual = Inicio;
    int i;
    i = 0;
    if (Inicio != NULL){
        do{
            // cout << "\n " << (actual->p1).getNombre();
            if (numberUser == i && contrass == ((actual->p1).getPassword())){
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
                cout << "Nombre: " << (actual->p1).getNombre();
                cout << "Edad: " << (actual->p1).getEdad();
                cout << "Password: ****** " ;
                
            }
            else{
                i = i+1;
                // cout << "Contraseña y/o Usuario Incorrecto \n";
            }
            actual = actual->sig;
            
        }while(actual != Inicio);
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}

