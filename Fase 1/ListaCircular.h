/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   ListaCircular.h
 * Author: Alex Rose
 *
 * Created on 6 de agosto de 2022, 09:42 AM
 */

#ifndef LISTACIRCULAR_H
#define LISTACIRCULAR_H

#include "nodocircu.h"
// #include "PersonaA.h"

#include <iostream>
using namespace std;



class ListaCircular {
public:
    // PersonaA p1;
    nodocircu*Inicio;
    nodocircu*Ultimo;

    ListaCircular() {
        Inicio = NULL;
        Ultimo = NULL;
    }
    void InsertarFinal(PersonaA p1);
    
    void Imprimir();
    void ModificarUsuario(string numberUser,  string contrass);
    void EliminarUsuario(string numberUser,  string contrass);
    void GrafoUsuarios();
    int BuscarUsuario(string numberUser,  string contrass);

    void InsertarEnOrdenReporte(PersonaA p1);
    void GrafoASCUsuarios();

private:
};

#endif /* ListaCircular_H */

