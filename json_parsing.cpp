/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/cppFiles/file.cc to edit this template
 */


/*
IINCLUDES NO BORRAR PENDEJO
*/
#include <iostream>
#include "json/json.h"
#include "json/json-forwards.h"
#include "jsoncpp.cpp"
#include <string>
// #include <char>
#include <fstream>
#include "json_parsing.h"   

using namespace std;
/*
IINCLUDES NO BORRAR PENDEJO
*/

class Persona {
 private:
  std::string nombre;
  int edad;
  int monedas;
  char password;

  void metodoPrivado() { std::cout << "Llamada privada dentro de la clase\n"; }

 public:
  // Constructor sin argumentos
  Persona() {
    std::cout << "Se llama al constructor sin argumentos\n";
    this->metodoPrivado();
  }
  // Constructor con nombre y edad
  Persona(std::string nombre, int edad,int monedas,char password) {
    this->edad = edad;
    this->nombre = nombre;
    this->monedas = monedas;
    this->password = password;
  }

  int getEdad() { return this->edad; }

  void setEdad(int edad) { this->edad = edad; }

  std::string getNombre() { return this->nombre; }

  void setNombre(std::string nombre) { this->nombre = nombre; }

  void saludar() {
    std::cout << "Hola, me llamo " << this->nombre << " y mi edad es "
              << this->edad << "\n";
  }
};





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

        // int monedas = users[i]["monedas"].get<int>();

        Persona p1("Luis",21,21,'a');

        int edad = p1.getEdad();
        cout << "edad: " << edad << endl;
    }
    
    
    //return 0;
}

