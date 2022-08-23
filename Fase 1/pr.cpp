/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   pr.cpp
 * Author: Alex Rose
 * 
 * Created on 6 de agosto de 2022, 09:42 AM
 */
#include "pr.h"
#include <iostream>

///////////// NUEVO
#include "sha256.h"
///////////// NUEVO

using namespace std;

void pr::Mostrar(int valor) {
    
    string sevice;
    sevice = "hola mundo ";
    cout << sevice << valor << endl;

    ///////////// NUEVO
    string msg;
	
	cout << "Escribe el mensaje:\n";
	cin >> ws;
	getline(cin, msg);

	string nuevo = SHA256::cifrar(msg);
	cout << "\nHash resultante: " << nuevo;
    ///////////// NUEVO

}

// void pr::Imprimir() {
//     nodosimple*aux = Inicio;
//     while (aux != NULL) {
//         cout <<"[" << aux->valor << "]->";
//         aux = aux->sig;
//     }
//     cout << ("NULL");
// }

