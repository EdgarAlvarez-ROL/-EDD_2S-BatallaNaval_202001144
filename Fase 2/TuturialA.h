#include <stdlib.h>
#include <string>
using namespace std;

class TutorialA{
   private:// Atributos
        int alto;
        int ancho;
        std::string xy;

  public:
    // Constructor,nos sirve para inicializar los atributos
    TutorialA(int _alto,int _ancho,std::string _xy){
        this->alto = _alto;
        this->ancho = _ancho;
        this->xy = _xy;
    }
    
    int getAlto() { return this->alto; }
    void setAlto(int alto) { this->alto = alto; }

    int getAncho(){ return this->ancho;};
    void setAncho(int ancho) { this->ancho = ancho; }
   
    std::string getXY() { return this->xy; }
    void setXY(std::string xy) { this->xy = xy; }
   

  };
  

