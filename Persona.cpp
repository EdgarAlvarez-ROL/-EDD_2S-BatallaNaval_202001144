// Archivo fuente de implementación de la clase Persona
#include "Persona.h" // Incluimos la definición (declaración) de la clase
#include <iostream> // Incluimos iostream para usar std::cout
using namespace std; // utilizaremos el espacio de nombres std para cout y string
// Constructor, asigna los valores iniciales de los datos de la persona
Persona::Persona(const string& nombre,int edad, int monedas, char password){
  this -> nombre = nombre; 
  this -> edad = edad;
  this -> monedas = monedas;
  this -> password = password;
}
// Saludo: la persona saluda y dice sus datos.
// void Persona::saluda(){
//   cout << "¡Hola! me llamo " << nombre 
//        << ", tengo " << edad << " años"
//        << ", peso " << peso << " kilos"
//        << " y mido " << estatura << " metros" << endl;
// }
// Cumple años: refleja los cambios en los atributos de la persona al haber pasado un año
// int Persona::cumpleAnios(){
//   float aumento_peso = 0;
//   float aumento_estatura = 0;
  
//   if (edad <= 20){
//     aumento_peso = 0.1;
//     aumento_estatura = 0.1;
//   }
//   edad += 1;
//   return edad;
// }