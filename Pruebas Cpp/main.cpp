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
#include "ListaSimple.cpp"
#include "json_parsing.h"
#include "json_parsing.cpp"
/*
 */

// #include "jsoncpp.cpp"

#include <cstdlib>
#include <iostream>


#include "json/json.h"
#include <string>
#include <fstream>

// #include "PersonaA.h"

#include "ListaCircular.h"
#include "ListaCircular.cpp"

using namespace std;

/*
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

    ListaCircular listaCircu;
    
    do
    {
      
        // FUNCIONA
        // pr prueba;
        // prueba.Mostrar(3);
        cout << "********** MENU **********\n";
        cout << " 1. Carga Masiva \n";
        cout << " 2. Registrar Usuario \n";
        cout << " 3. Login \n";
        cout << " 4. Reportes \n";
        cout << " 0. SALIR del juego \n";

        cout << "Ingrese una opcion a ejecutar\n";
        cin >> opcion;
        
        
        // cout << "\nUsted a ingresado la opcion: " << opcion << endl;
        switch(opcion){
            case 1:               
                cout << " 1. Carga Masiva \n";
                //
                json_parsing lectorJson;
                lectorJson.lector();
                
                
            //    g++ main.cpp -o main
                // //FUNCIONA 
                
                
                //system("pause>nul"); // Pausa
                cout << "\n";
                break;
            case 2:
                {
                cout << " 2. Registrar Usuario \n";
                //system("pause>nul"); // Pausa

                string nickTemp, passwordTemp;
                int edadTemp;
                cout << "Ingrese su Nick: ";
                cin >> nickTemp;

                cout << "Ingrese su Edad: ";
                cin >> edadTemp;

                cout << "Ingrese su Password: ";
                cin >> passwordTemp;

                
                
                PersonaA pcua = PersonaA(nickTemp,edadTemp,0,passwordTemp);
                // Persona pcua(nickTemp,edadTemp,0,passwordTemp);
                cout << "Usuario Registrado como: " << pcua.getNombre() << " con edad : " << pcua.getEdad() <<  " años inicia con: " << pcua.getMonedas() << " monedas y su contraseña es: " << pcua.getPassword() << "\n";
                listaCircu.InsertarFinal(pcua);
                listaCircu.Imprimir();

                // ListaSimple pruebas;
                // pruebas.InsertarFinal(1);
                
                
                cout << "\n";
                break;
                }
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
    // system("PAUSE");
    return 0;
}





