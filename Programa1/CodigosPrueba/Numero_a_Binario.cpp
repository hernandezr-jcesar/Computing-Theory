#include <iostream>
using namespace std;

int main(){
	cout << "Convertidor de numero a binario";
	
	cout << "Ingrese un numero entero positivo:" << endl;
	int numero;
	string binario = "";
	cin >> numero;
	if(numero > 0) {
		while(numero > 0){
			if(numero%2 == 0){
				binario = "0" + binario;
			}else {
				binario = "1" + binario;
			}
			numero = (int) numero/2;
		}
	}else if(numero == 0){
		binario = "0";
	}else{
		binario ="imposible";
	}
	cout << "El resultado de la conversion es: " << binario << endl;
	return 0;
}
