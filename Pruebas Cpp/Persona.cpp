#include <iostream>
#include <string>
// #include "Persona.h"

using namespace std;

class Persona {
 private:
  std::string nombre;
  int edad;
  int monedas;
  std::string password;

  void metodoPrivado() { std::cout << "Llamada privada dentro de la clase\n"; }

 public:
  // Constructor sin argumentos
  Persona() {
    std::cout << "Se llama al constructor sin argumentos\n";
    this->metodoPrivado();
  }
  // Constructor con nombre y edad
  Persona(std::string nombre, int edad,int monedas,std::string password) {
    this->edad = edad;
    this->nombre = nombre;
    this->monedas = monedas;
    this->password = password;
  }

  int getEdad() { return this->edad; }
  void setEdad(int edad) { this->edad = edad; }

  std::string getNombre() { return this->nombre; }
  void setNombre(std::string nombre) { this->nombre = nombre; }

  int getMonedas(){ return this->monedas;};
  void setMonedas(int monedas) { this->monedas = monedas; }

  std::string getPassword() { return this->password; }
  void setPassword(std::string nombre) { this->password = password; }
  
};


