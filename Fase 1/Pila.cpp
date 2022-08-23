/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Pila.cpp
 * Author: Alex Rose
 * 
 * Created on 13 de agosto de 2022, 10:11 AM
 */

#include "Pila.h"

void Pila::push(TutorialA valor) {
    nodopila*nuevo = new nodopila();
    (nuevo->valor).setAlto(valor.getAlto());
    (nuevo->valor).setAncho(valor.getAncho());
    (nuevo->valor).setXY(valor.getXY());

    if (Inicio == NULL) {
        Inicio = nuevo;
    } else {
        nuevo->sig=Inicio;
        Inicio=nuevo;
    }
}

void Pila::pop() {
    nodopila*aux =Inicio;
    Inicio=aux->sig;
}

void Pila::Imprimir() {
    nodopila*aux = Inicio;
    cout << "\nTutorial: \n";
    cout << "   Tablero: \n";
    cout << "       Ancho: " + std::to_string((aux->valor).getAncho()) + "\n        Alto: " + std::to_string((aux->valor).getAlto()) + "\n" ;
    cout << "   Movimientos: \n";
    while (aux != NULL) {
        cout <<"        [" << (aux->valor).getXY() << "]  \n";
        aux = aux->sig;
    }
}




void Pila::GrafoPilaTuto() {
    string dot = "";
    dot = dot + "\ndigraph G {\n";
    dot = dot + "label=\"Pila del Tutorial\";\n";
    dot = dot + "node [shape=box];\n";

    nodopila*aux = Inicio;
    dot = dot + "//agregar nodos\n";
    dot = dot + "P1Cabeza" + "[label=\"" + "Ancho: " + std::to_string((aux->valor).getAncho()) + " | Alto: " + std::to_string((aux->valor).getAlto()) + "\"];\n";
    int i = 0;
    if (Inicio != NULL){
        while (aux != NULL) {
            dot = dot + "Ptuto" + std::to_string(i) + "[label=\"" + ((aux->valor).getXY()) + "\"];\n";
            // cout <<"        [" << (aux->valor).getXY() << "]  \n";
            aux = aux->sig;
            i = i + 1;
        }
  

        dot = dot + "//Enlazar imagenes\n";
        dot = dot + "{rank=same;\n";

        dot =  dot +"P1nodoZ->";
        
        /**CONECTANDO NODOS DE PRINCIPIO A FIN**/
        aux = Inicio;
        i = 0;
        while (aux != NULL) {
        dot = dot + "Ptuto" + std::to_string(i);
        if (aux->sig != NULL) {
            dot = dot + "->";
        }
        aux = aux->sig;
        i = i + 1;
        }


        

    dot = "\n" +dot + "\n";        
    dot = dot + "\n}\n";
    dot = dot + "}\n";

    cout << dot;

    //------->escribir archivo
    ofstream file;
    file.open("PilaTutorial.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng PilaTutorial.dot -o  PilaTutorial.png"));

    //------>abrir archivo
    system(("PilaTutorial.png"));
    
    }else{
        cout << "LA LISTA ESTA VACIA";
    }
 
}








