#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

class PersonaA{
   private:// Atributos
        int edad;
        std::string nombre;
        int monedas;
        std::string password;

      // void metodoPrivado() { std::cout << "Llamada privada dentro de la clase\n"; }

  public:
    // // Constructor sin argumentos
    // PersonaA() {
    //   nombre = "";
    //   edad = 0;
    //   monedas = 0;
    //   password = "";
    // }
    // Constructor,nos sirve para inicializar los atributos
    PersonaA(std::string _nombre,int _edad,int _monedas, std::string _password){
        this->edad = _edad;
        this->nombre = _nombre;
        this->monedas = _monedas;
        this->password = _password;
    }
    
    int getEdad() { return this->edad; }
    void setEdad(int edad) { this->edad = edad; }

    std::string getNombre() { return this->nombre; }
    void setNombre(std::string nombre) { this->nombre = nombre; }

    int getMonedas(){ return this->monedas;};
    void setMonedas(int monedas) { this->monedas = monedas; }

    std::string getPassword() { return this->password; }
    void setPassword(std::string password) { this->password = password; }


   

  };
  

