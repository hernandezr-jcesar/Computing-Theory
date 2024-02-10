#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>

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
int limitedeunos(int n){
	int lu=0;//limite de unos
	for(int i=0; i < n; i++){
		lu =((2*lu) +1);	
	}
	return lu;
}
string llenar0(string cadena, int limite){
	int conta;
	
	int largo = cadena.size();
	
	string cadenacompleta = "";
	cadenacompleta = cadena;
	
	int cant0 = limite-largo;
	if (largo < limite){
		for(int i = 0; i < cant0;i++){
			cadenacompleta = "0" + cadenacompleta;
		}
	}
	return cadenacompleta;
}
void sigmaasterisco(int k){
	
	ofstream archivo;
	archivo.open("Sigmaasterisco10.txt");
	for(int contador=0;contador <= k; contador++){
		
		int limite = contador;
		string binario="";
		
		for(int conta = 0; conta <= limitedeunos(limite);conta++){
			binario = Decimal_A_Binario(conta);
			
			if (limitedeunos(limite) == 0){
			archivo <<"{"<<"e";
			}
			if(binario.size() < limite){
				archivo <<","<<llenar0(binario,limite);
			}
			if(binario.size() == limite){
				archivo <<","<< binario ;
			 } 			
		}
				
	}
	archivo << "}.";
	archivo.close();
}
int main(){

	int in;
	cin >> in;
	sigmaasterisco(in);

	return 0;
}
