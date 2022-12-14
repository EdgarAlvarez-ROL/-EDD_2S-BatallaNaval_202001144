/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   ListaPrincipal.cpp
 * Author: Alex Rose
 * 
 * Created on 20 de agosto de 2022, 09:36 AM
 */

#include "ListaPrincipal.h"
// #include <windows.h> 
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>   // std::cout

void ListaPrincipal::Imprimir() {
    nodoprincipal*aux = Inicio;
    while (aux != NULL) {
        cout << "[" << ((aux->valor).getCategoria()) << "]->";
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            cout << "[" << (auxI->valor).getNombre() << "]->";
            auxI = auxI->sig;
        }
        cout << ("NULL");
        cout << ("\n |-> ");
        aux = aux->sig;
    }
    cout << ("NULL");
}

void ListaPrincipal::ImprimirArticulos() {
    nodoprincipal*aux = Inicio;
    while (aux != NULL) {
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            cout << ((auxI->valor).getId()) << "\t" << (auxI->valor).getNombre() << "\t \t" << (auxI->valor).getCategoria() << "\t" << (auxI->valor).getPrecio();
            cout << "\n";
            auxI = auxI->sig;
        }
        aux = aux->sig;
    }
}


void ListaPrincipal::GenerarGrafo() {
    string dot = "";
    dot = dot + "\ndigraph G {\n";
    dot = dot + "label=\"Lista de Listas de los Articulos\";\n";
    dot = dot + "node [shape=box];\n";

    nodoprincipal*aux = Inicio;
    dot = dot + "//agregar nodos\n";
    while (aux != NULL) {
        dot = dot + "N" + std::to_string((aux->valor).getId()) + "[label=\"" + (aux->valor).getCategoria() + "\"];\n";
        /*CAPAS DE CADA NODO PRINCIPAL OSEA categoria*/
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            dot = dot + "C" + std::to_string((auxI->valor).getId()) + "[label=\"" + (auxI->valor).getNombre() + "\"];\n";
            auxI = auxI->sig;
        }            
        /*CAPAS DE CADA NODO PRINCIPAL OSEA categoria*/
        aux = aux->sig;
    }


    dot = dot + "//Enlazar imagenes\n";
    dot = dot + "{rank=same;\n";
    aux = Inicio;
    while (aux != NULL) {

        dot = dot + "N" + std::to_string((aux->valor).getId());
        if (aux->sig != NULL) {
            dot = dot + "->";
        }
        aux = aux->sig;
    }
    /*CONECTAR CADA NODO CON CADA CAJA*/
    dot = "\n" +dot + "\n";
    dot = dot + "\n}\n";
    aux = Inicio;
    while (aux != NULL) {

        dot = dot + "N" + std::to_string((aux->valor).getId());
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            dot = dot + "->" +  "C" + std::to_string((auxI->valor).getId());
            
            // if (auxI->sig != NULL) {
            //     dot = dot + "->";
            // }
            auxI = auxI->sig;
        }   
        aux = aux->sig;
        dot = "\n" +dot + "\n";
    }
    /*CONECTAR CADA NODO CON CADA CAJA*/

    
    dot = dot + "}\n";

    cout << dot;
    
    //------->escribir archivo
    ofstream file;
    file.open("Pruebas.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng Pruebas.dot -o  Pruebas.png"));

    //------>abrir archivo
    system(("Pruebas.png"));
    
}

void ListaPrincipal::Insertar(ArticuloA valor, string categoria) {
    if (Inicio == NULL) {//lista se encuentra vacia
        nodoprincipal*nuevo = new nodoprincipal();
        // ((nuevo->valor).getCategoria()) = categoria;      /////////////////////////MIS DUDAS///////////////////
        ((nuevo->valor).setCategoria(categoria));
        ((nuevo->valor).setId(valor.getId()));
        ((nuevo->valor).setNombre(valor.getNombre()));
        ((nuevo->valor).setPrecio(valor.getPrecio()));
        ((nuevo->valor).setSrc(valor.getSrc()));
        // cout << "NOMBRE del insertar: " << (nuevo->valor).getNombre() << "\n";

        nuevo->listainterna.InsertarEnOrden(valor);
        Inicio = nuevo;
    } else {//la lista no se encuentra vacia
        nodoprincipal*busqueda = BuscarPrincipal(Inicio, categoria);
        nodoprincipal*nuevo = new nodoprincipal();
        // ((nuevo->valor).getCategoria()) = categoria; ///////////////////// MIS DUDAS /////////////////////
        ((nuevo->valor).setCategoria(categoria));
        ((nuevo->valor).setId(valor.getId()));
        ((nuevo->valor).setNombre(valor.getNombre()));
        ((nuevo->valor).setPrecio(valor.getPrecio()));
        ((nuevo->valor).setSrc(valor.getSrc()));
        // cout << "NOMBRE del insertar: " << (nuevo->valor).getNombre() << "\n";

        nuevo->listainterna.InsertarEnOrden(valor);
        if (busqueda == NULL) {//como no hay categoria insertamos al final una nueva
            nodoprincipal*auxActual = Inicio;
            while (auxActual != NULL) {
                if (auxActual->sig == NULL) {
                    auxActual->sig = nuevo;
                    break;
                }
                auxActual = auxActual->sig;
            }
        } else {//si la categoria existe se inserta en la misma
            busqueda->listainterna.InsertarEnOrden(valor);
        }
    }



    //    nodoprincipal*nuevo = new nodoprincipal();
    //    nuevo->valor = valor;
    //
    //    if (Inicio == NULL) {
    //        Inicio = nuevo;
    //    } else {
    //        nodoprincipal*auxActual = Inicio;
    //
    //        while (auxActual != NULL) {
    //            if (auxActual->sig == NULL) {
    //                auxActual->sig = nuevo;
    //                break;
    //            }
    //            auxActual = auxActual->sig;
    //        }
    //    }
}

nodoprincipal* ListaPrincipal::BuscarPrincipal(nodoprincipal* inicioL, string categoria) {
    if (inicioL == NULL) {
        return inicioL;
    } else {
        nodoprincipal*auxActual = inicioL;
        while (auxActual != NULL) {
            if ((auxActual->valor).getCategoria() == categoria) {
                break;
            }
            auxActual = auxActual->sig;
        }
        return auxActual;
    }
}
