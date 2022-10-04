#include <stdlib.h>
#include <string>
using namespace std;

class ArticuloA{
   private:// Atributos
        std::string categoria;
        int id;
        int precio;
        std::string src;
        std::string nombre;

  public:
    // Constructor,nos sirve para inicializar los atributos
    ArticuloA(std::string _categoria,int _id,int _precio, std::string _nombre, std::string _src){
        this->id = _id;
        this->categoria = _categoria;
        this->precio = _precio;
        this->src = _src;
        this->nombre = _nombre;
    }
    
    int getId() { return this->id; }
    void setId(int id) { this->id = id; }

    std::string getCategoria() { return this->categoria; }
    void setCategoria(std::string categoria) { this->categoria = categoria; }

    int getPrecio(){ return this->precio;};
    void setPrecio(int precio) { this->precio = precio; }

    std::string getSrc() { return this->src; }
    void setSrc(std::string src) { this->src = src; }

    std::string getNombre() { return this->nombre; }
    void setNombre(std::string nombre) { this->nombre = nombre; }
   
  };
  

