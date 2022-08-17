/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/cppFiles/file.cc to edit this template
 */


#include <iostream>
#include "json/json.h"
//#include "json/json-forwards.h"
// #include "jsoncpp.cpp"
#include <string>
#include <fstream>
#include "json_parsing.h"   

using namespace std;


void json_parsing::lector(){
    
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
    
    
    const Json::Value users = actualJson["usuarios"];
   
    for(int i = 0; i < users.size(); i = i + 1){
        //listaUsuarios->
        
        cout << i << endl;
        cout << users[i]["nick"] << endl;
    }
    
    
    //return 0;
}




