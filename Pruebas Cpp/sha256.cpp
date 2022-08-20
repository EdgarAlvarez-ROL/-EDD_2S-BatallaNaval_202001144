#include "sha256.h"

using namespace std;

int main() {
	string msg;
	
		cout << "Escribe el mensaje:\n";
		cin >> ws;
		getline(cin, msg);

		string nuevo = SHA256::cifrar(msg);
		cout << "\nHash resultante: " << nuevo;

		// _getch();
		// system("cls");
		cout << "\n";
	
	return 0;
}