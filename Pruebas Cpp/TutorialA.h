#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

class ArticuloA{
   private:// Atributos
        int ancho;
        int alto;
        std::string movimientos;

  public:
    // Constructor,nos sirve para inicializar los atributos
    ArticuloA(int _ancho,int _alto, std::string _movimientos){
        this->ancho = _ancho;
        this->alto = _alto;
        this->movimientos = _movimientos;
    }

    int getAncho() { return this->ancho; }
    void setAncho(int ancho) { this->ancho = ancho; }

    int getAlto() { return this->alto; }
    void setAlto(int alto) { this->alto = alto; }
    
    std::string getMovimientos() { return this->movimientos; }
    void setMovimientos(std::string movimientos) { this->movimientos = movimientos; }
   
  };
  

