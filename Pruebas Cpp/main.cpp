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

#include "ListaInterna.h"
#include "ListaInterna.cpp"
#include "ListaPrincipal.h"
#include "ListaPrincipal.cpp"

#include "Pila.h"
#include "Pila.cpp"

/////////////
// #include<stdio.h>
// #include<conio.h>


using namespace std;


// INICIO -Variables GLOBALES
    ListaCircular listaCircu;
    ListaPrincipal listaArticulos;
    Pila pilaTutorial;
    // ListaPrincipal listaPrincipal;
    
// FIN    -Variables GLOBALES

int lectorJson(){
    
    // Usando el fstream para tomar la ruta del archivo
    ifstream file("DATOS.json");
    Json::Value actualJson;
    Json::Reader reader;
    
    // Usando Reader para parsear el Json osea leerlo
    reader.parse(file, actualJson);
    
    // Ahora obtendremos la data del JSON
    //cout << "Total JSON data: \n" << actualJson << endl;
    
    // Ahora obtendremos los datos INDIVIDUALMENTE
    // Numero de elementos dentro del JSON
    //cout << "Objeto de la Rama Principal de JSON: " << actualJson.size() << endl;
    
    // USUARIOS
    const Json::Value users = actualJson["usuarios"];
    for(int i = 0; i < users.size(); i = i + 1){

        string nick = users[i]["nick"].asString();

        string edadTemp = (users[i]["edad"].asString());
        int edad = std::atoi(edadTemp.c_str());

        string monTemp = (users[i]["monedas"].asString());
        int monedas = std::atoi(monTemp.c_str());

        string password = users[i]["password"].asString();

        // cout << edad << endl;
        PersonaA usuario(nick,edad,monedas,password);
        // cout << usuario.getNombre() << " "  << usuario.getEdad() << " " << usuario.getMonedas() << " " << usuario.getPassword() << endl;
        
        listaCircu.InsertarFinal(usuario);

    }

    const Json::Value articulos = actualJson["articulos"];
    for(int i=0; i < articulos.size(); i = i + 1){

        string idTemp = articulos[i]["id"].asString();
        int id = std::atoi(idTemp.c_str());

        string categoria = articulos[i]["categoria"].asString();

        string precioTemp = articulos[i]["precio"].asString();
        int precio = std::atoi(precioTemp.c_str());

        string nombre = articulos[i]["nombre"].asString();

        string src = articulos[i]["src"].asString();

        ArticuloA nuevoArticulo = ArticuloA(categoria,id,precio,nombre,src); //categoria id precio nombre src
        listaArticulos.Insertar(nuevoArticulo,nuevoArticulo.getCategoria());

    }

    const Json::Value tuto = actualJson["tutorial"];
    string anchoTemp = tuto["ancho"].asString();
    int ancho = std::atoi(anchoTemp.c_str());

    string altoTemp = tuto["alto"].asString();
    int alto = std::atoi(altoTemp.c_str());

    const Json::Value movs = tuto["movimientos"];
    for(int i=0; i < movs.size(); i = i + 1){
        string xM = movs[i]["x"].asString();
        string yM = movs[i]["y"].asString();

        string coordenada = xM +  "," + yM;
        // cout << coordenada;

        TutorialA tutorial = TutorialA(ancho,alto,coordenada);
        pilaTutorial.push(tutorial);
    }    
    

    return 0;
}
   

int main()
{
    int opcion = 0;
    char opcionLogin = 'z';

    // listaPrincipal.Insertar(1,1);
    
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

        cout << "Ingrese una opcion a ejecutar: ";
        cin >> opcion;
        
        
        // cout << "\nUsted a ingresado la opcion: " << opcion << endl;
        switch(opcion){
            case 1:   {           
                cout << " 1. Carga Masiva \n";
                //
                // json_parsing lectorJson;
                // lectorJson.lector();

                lectorJson();
                // Persona lisTEmpPersonas[1000];
                // Persona lisTEmpPersonas = lectorJson.lector();
                
                cout << "\n====Carga del Archivo con Exitos====\n";
            //    g++ main.cpp -o main
                // //FUNCIONA 
                
                
                //system("pause>nul"); // Pausa
                cout << "\n";
                break;
                } 
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
            case 3:{
                int numberUser;
                string contrass;
                cout << " 3. Login \n";
                cout << "   a. Editar Informacion \n";
                cout << "   b. Eliminar Cuenta \n";
                cout << "   c. Ver el Tutorial \n";
                cout << "   d. Ver articulos de la tienda \n";
                cout << "   e. Realizaqr Movimientos \n";
                cout << "   f. Salir al menu principal \n";

                cout << "Ingrese una opcion a ejecutar\n";
                cin >> opcionLogin;

                switch (opcionLogin)
                {
                case 'a':{
                    cout << "\n======Editar Informacion======";
                    listaCircu.Imprimir();
                    cout << "\nIngrese su numero de usuario: ";
                    cin >> numberUser;
                    cout << "Ingrese su contraseña: ";
                    cin >> contrass;

                    listaCircu.ModificarUsuario(numberUser,contrass);
                    
                    break;
                    }
                case 'b':{
                    cout << "\n======Eliminar Cuenta======";
                    listaCircu.Imprimir();
                    cout << "\nIngrese su numero de usuario: ";
                    cin >> numberUser;
                    cout << "Ingrese su contraseña: ";
                    cin >> contrass;
                    listaCircu.EliminarUsuario(numberUser, contrass);
                    break;
                    }
                case 'c':{
                    cout << "\n======Tutorial======";
                    pilaTutorial.Imprimir();
                    break;
                    }
                case 'd':
                    // listaArticulos.Imprimir();l
                    break;
                case 'e':
                    cout << "e";
                    break;
                case 'f':
                    // cout << "a";
                    break;
                
                
                default:cout << "Usted ha ingresado una opción incorrecta" << "\n" << endl;
                    break;
                }
                


                //system("pause>nul"); // Pausa
                cout << "\n";
                break;
            }
            case 4:{
                cout << " 4. Reportes \n";
                // listaArticulos.GenerarGrafo(); // LISTA DE LISTAS
                // listaCircu.GrafoUsuarios();
                pilaTutorial.GrafoPilaTuto();
                // system("pause>nul"); // Pausa
                cout << "\n";
                break; 
            }
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



