#include <iostream>
using namespace std;


string Decimal_A_Binario(int numero){
	string binario = "";
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
	}
	return binario;
}
int main(){
	int numero;
	cin >> numero;	
	cout << Decimal_A_Binario(numero);
}