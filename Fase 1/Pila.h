/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Pila.h
 * Author: Alex Rose
 *
 * Created on 13 de agosto de 2022, 10:11 AM
 */

#ifndef PILA_H
#define PILA_H
#include "NodoPila.h"

#include <iostream>
using namespace std;

class Pila {
public:
    nodopila*Inicio;

    Pila() {
        Inicio = NULL;
    }
    void push(TutorialA valor);
    void pop();
    void peck(); 
    void Imprimir(); 
    void GrafoPilaTuto();
private:

};

#endif /* PILA_H */

