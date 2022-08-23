/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   NodoInterno.h
 * Author: Alex Rose
 *
 * Created on 20 de agosto de 2022, 09:37 AM
 */

#ifndef NODOINTERNO_H
#define NODOINTERNO_H
#include <stddef.h>
#include "ArticuloA.h"

class nodointerno {
public:
    ArticuloA valor = ArticuloA("",0,0,"",""); // categoria id precio nombre src
    ArticuloA p2 = ArticuloA("",0,0,"","");
    nodointerno*sig;
    nodointerno() {
        sig = NULL;
        valor = p2;
    }
private:
};

#endif /* NODOINTERNO_H */

