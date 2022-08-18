//Definición de la clase persona -> archivo "Persona.h"
//siempre es buena idea usar macros del preprocesador para evitar compilar varias veces el mismo archivo
#ifndef PERSONA_H 
#define PERSONA_H
#include <string>
class Persona //Declaramos la clase con el nombre Persona
{
private:     //a partir de aquí todos los miembros serán privados
//los datos miembro pueden ser cualquier tipo de dato, incluso otras clases como string
   
//             //métodos privados
//   float aumentaEstatura(float metros){return estatura += metros}; //función inline
//   float aumentaPeso(float kilogramos){return peso += kilogramos};

public:      //a patir de aquí todas las declaraciones serán de acceso público
std::string nombre;
  int edad;
  int monedas;
  char password;  
  Persona(const std::string& nombre,int edad, int monedas, char password); // Constructor
//   void saluda();
//   int cumpleAnios();
};
#endif