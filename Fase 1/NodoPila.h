/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Nodo.h
 * Author: Alex Rose
 *
 * Created on 13 de agosto de 2022, 10:11 AM
 */

#ifndef NODOPILA_H
#define NODOPILA_H

#include <stddef.h>
#include "TuturialA.h"
class nodopila {
public:
    // int valor;
    TutorialA valor = TutorialA(0,0,"");
    TutorialA pT = TutorialA(0,0,"");
    nodopila*sig;
    nodopila() {
        sig = NULL;
        valor = pT;
    }
private:
};

#endif /* nodopila */

