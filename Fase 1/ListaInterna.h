/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   ListaInterna.h
 * Author: Alex Rose
 *
 * Created on 20 de agosto de 2022, 09:36 AM
 */

#ifndef LISTAINTERNA_H
#define LISTAINTERNA_H

#include "NodoInterno.h"

#include <iostream>

using namespace std;

class ListaInterna {
public:
    nodointerno*Inicio;

    ListaInterna() {
        Inicio = NULL;
    }
    void InsertarFinal(ArticuloA valor);
    void InsertarEnOrden(ArticuloA valor);
    void InsertarEnOrdenDESC(ArticuloA valor);
    void Imprimir();
    void GrafoArticulosASC();
private:
};

#endif /* LISTAINTERNA_H */

