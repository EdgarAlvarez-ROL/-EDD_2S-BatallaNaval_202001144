/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   NodoPrincipal.h
 * Author: Alex Rose
 *
 * Created on 20 de agosto de 2022, 09:37 AM
 */

#ifndef NODOPRINCIPAL_H
#define NODOPRINCIPAL_H
#include <stddef.h>

#include "ListaInterna.h"


class nodoprincipal {
public:
    //----valores
    ListaInterna listainterna;
    ArticuloA valor = ArticuloA("",0,0,"",""); // categoria id precio nombre src
    ArticuloA p2 = ArticuloA("",0,0,"","");
    //----apuntadores
    nodoprincipal*sig;
    
    nodoprincipal() {
        sig = NULL;
        valor = p2;
    }
private:
};

#endif /* NODOPRINCIPAL_H */

