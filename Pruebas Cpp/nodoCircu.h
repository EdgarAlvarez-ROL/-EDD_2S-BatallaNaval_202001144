/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   nodocircu.h
 * Author: Alex Rose
 *
 * Created on 6 de agosto de 2022, 09:37 AM
 */

#ifndef NODOCIRCU_H
#define NODOCIRCU_H
#include <stddef.h>
#include "PersonaA.h"    

class nodocircu {
public:
    PersonaA p1 = PersonaA("",0,0,"");;
    

    nodocircu*sig;
    nodocircu() {
        sig = NULL;
        p1 = PersonaA("",0,0,"");
        // valor = 0;
    }
private:
};
#endif /* NODOCIRCU_H */

