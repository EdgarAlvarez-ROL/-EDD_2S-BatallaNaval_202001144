/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Alex Rose
 *
 * Created on 6 de agosto de 2022, 09:29 AM
 */

/*
 *NODOS DE OTRAS LISTAS 
 */
#include "ListaSimple.h"
#include "json_parsing.h"
/*
 */

#include <cstdlib>
#include <iostream>


#include "json/json.h"
#include <string>
#include <fstream>


//#include "jsoncpp.cpp"

using namespace std;

/*
 * 
int main(int argc, char** argv) {

    ListaSimple pruebas;
    pruebas.InsertarEnOrden(7);
    pruebas.InsertarEnOrden(1);
    pruebas.InsertarEnOrden(4);
    pruebas.InsertarEnOrden(5);
    pruebas.InsertarEnOrden(6);
    pruebas.InsertarEnOrden(8);
    pruebas.Imprimir();
    return 0;
}
 */


int main()
{
    int opcion = 0;
    do
    {
        cout << "********** MENU **********\n";
        cout << " 1. Carga Masiva \n";
        cout << " 2. Registrar Usuario \n";
        cout << " 3. Login \n";
        cout << " 4. Reportes \n";
        cout << " 0. SALIR del juego \n";

        cout << "Ingrese una opción a ejecutar\n";
        cin >> opcion;
        
        
        cout << "\nUsted a ingresado la opcion: " << opcion << endl;
        switch(opcion){
            case 1:               
                cout << " 1. Carga Masiva \n";
                //
                json_parsing leerFile;
                leerFile.lector();
               
                //FUNCIONA


                
                //system("pause>nul"); // Pausa
                cout << "\n";
                break;
            case 2:
                
                cout << " 2. Registrar Usuario \n";
                //system("pause>nul"); // Pausa
                cout << "\n";
                break;
            case 3:
                cout << " 3. Login \n";
                //system("pause>nul"); // Pausa
                cout << "\n";
                break;
            case 4:
                cout << " 4. Reportes \n";
                //system("pause>nul"); // Pausa
                cout << "\n";
                break; 
            case 0:
                // Lista de instrucciones de la opción 1                
                cout << "\n";
                break;
                
            default: cout << "Usted ha ingresado una opción incorrecta" << "\n" << endl;
        }
    }
    //Mostramos el menú hasta que la opción sea cero
    while(opcion != 0);
    //system("PAUSE");
    return 0;
}






