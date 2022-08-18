/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   nodoSimple.h
 * Author: Alex Rose
 *
 * Created on 6 de agosto de 2022, 09:37 AM
 */

#ifndef PERSONA_H
#define PERSONA_H
#include <stddef.h>

#include <iostream>
#include <string>

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



#endif /* PERSONA */

