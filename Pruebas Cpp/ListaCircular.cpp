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

/*

void insertartodo(){
    node nuevo new nodo();
    cout << Ingrese el dato que contendra el nuevo Nodo:";
    cin >> nueve->dato;
    if(primero -- NULL){
        primero nuevo;
        primere->siguiente primera;
        ultimo primera
                            nuevo;ultima siguiente
        nuevo->siguiente primeros
        ultimo nuevo;
   1
    cout <<"\nNodo Inbgresade\n\n";
    Jelse(

*/

void ListaCircular::Imprimir() {
    // nodocircu*aux = Inicio;
    nodocircu*actual = new nodocircu();
    actual = Inicio;
    if (Inicio != NULL){
        do{
            cout << "\n " << (actual->p1).getNombre();
            actual = actual->sig;
            
        }while(actual != Inicio);
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
    



    
}

/*
void ListaCircular::InsertarEnOrden(PersonaA p1) {
    nodocircu*nuevo = new nodocircu();
    nuevo->p1 = p1;
    if (Inicio == NULL) {//Si la lista se encuentra vacia
        Inicio = nuevo;
    } else {//si la lista no esta vacia
        nodocircu*auxActual = Inicio;
        nodocircu*auxSiguiente;
        while (auxActual != NULL) {
            auxSiguiente = auxActual->sig;
            if (nuevo->p1 < auxActual->p1) {//insertar al inicio de la lista por que es menor
                nuevo->sig = auxActual;
                Inicio = nuevo;
                break;
            } else if (auxSiguiente == NULL) {//insertar al final de la lista
                auxActual->sig = nuevo;
                break;
            } else if (nuevo->p1 < auxSiguiente->p1) {//insertar en medio de la lista
                auxActual->sig = nuevo;
                nuevo->sig = auxSiguiente;
                break;
            }
            auxActual = auxActual->sig;
        }
    }
}

void ListaCircular::Imprimir() {
    nodocircu*aux = Inicio;
    while (aux != NULL) {
        cout <<"[" << aux->p1 << "]->";
        aux = aux->sig;
    }
    cout << ("NULL");
}

*/