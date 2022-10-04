/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   ListaInterna.cpp
 * Author: Alex Rose
 * 
 * Created on 20 de agosto de 2022, 09:36 AM
 */

#include "ListaInterna.h"
void ListaInterna::InsertarFinal(ArticuloA valor) {
    nodointerno*nuevo = new nodointerno();
    nuevo->valor = valor;

    if (Inicio == NULL) {
        Inicio = nuevo;
    } else {
        nodointerno*auxActual = Inicio;

        while (auxActual != NULL) {
            if (auxActual->sig == NULL) {
                auxActual->sig = nuevo;
                break;
            }
            auxActual = auxActual->sig;
        }
    }


}

void ListaInterna::InsertarEnOrden(ArticuloA valor) {
    nodointerno*nuevo = new nodointerno();
    nuevo->valor = valor;
    if (Inicio == NULL) {//Si la lista se encuentra vacia
        Inicio = nuevo;
    } else {//si la lista no esta vacia
        nodointerno*auxActual = Inicio;
        nodointerno*auxSiguiente;
        while (auxActual != NULL) {
            auxSiguiente = auxActual->sig;
            if (((nuevo->valor).getPrecio()) < ((auxActual->valor).getPrecio())) {//insertar al inicio de la lista por que es menor
                nuevo->sig = auxActual;
                Inicio = nuevo;
                break;
            } else if (auxSiguiente == NULL) {//insertar al final de la lista
                auxActual->sig = nuevo;
                break;
            } else if (((nuevo->valor).getPrecio()) < ((auxSiguiente->valor.getPrecio()))) {//insertar en medio de la lista
                auxActual->sig = nuevo;
                nuevo->sig = auxSiguiente;
                break;
            }
            auxActual = auxActual->sig;
        }
    }
}



void ListaInterna::InsertarEnOrdenDESC(ArticuloA valor) {
    nodointerno*nuevo = new nodointerno();
    nuevo->valor = valor;
    if (Inicio == NULL) {//Si la lista se encuentra vacia
        Inicio = nuevo;
    } else {//si la lista no esta vacia
        nodointerno*auxActual = Inicio;
        nodointerno*auxSiguiente;
        while (auxActual != NULL) {
            auxSiguiente = auxActual->sig;
            if (((nuevo->valor).getPrecio()) > ((auxActual->valor).getPrecio())) {//insertar al inicio de la lista por que es menor
                nuevo->sig = auxActual;
                Inicio = nuevo;
                break;
            } else if (auxSiguiente == NULL) {//insertar al final de la lista
                auxActual->sig = nuevo;
                break;
            } else if (((nuevo->valor).getPrecio()) > ((auxSiguiente->valor.getPrecio()))) {//insertar en medio de la lista
                auxActual->sig = nuevo;
                nuevo->sig = auxSiguiente;
                break;
            }
            auxActual = auxActual->sig;
        }
    }
}



void ListaInterna::Imprimir() {
    nodointerno*aux = Inicio;
    while (aux != NULL) {
        cout <<"[" << (aux->valor).getCategoria() << "]->";
        aux = aux->sig;
    }
    cout << ("NULL");
}


void ListaInterna::GrafoArticulosASC() {
    string dot = "";
    dot = dot + "\ndigraph G {\n";
    dot = dot + "label=\"Lista de Usuarios\";\n";
    dot = dot + "node [shape=box];\n";

    nodointerno*actual = Inicio;
    dot = dot + "//agregar nodos\n";

    while (actual != NULL) {
        // cout <<"[" << (aux->p1).getEdad() << "]->";
        dot = dot + "Arti" + std::to_string((actual->valor).getId()) + "[label=\"" + " Articulo: " + (actual->valor).getNombre() + ", Precio:" + std::to_string((actual->valor).getPrecio()) + "\"];\n";
        actual = actual->sig;
    }
    
    dot = dot + "//Enlazar imagenes\n";
    dot = dot + "{rank=same;\n";
    /**CONECTANDO NODOS DE PRINCIPIO A FIN**/
    actual = Inicio;
    while (actual != NULL) {
        dot = dot + "Arti" + std::to_string((actual->valor).getId());
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
    file.open("ArticulosOrdenASC.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng ArticulosOrdenASC.dot -o  ArticulosOrdenASC.png"));

    //------>abrir archivo
    system(("ArticulosOrdenASC.png"));
    


}
