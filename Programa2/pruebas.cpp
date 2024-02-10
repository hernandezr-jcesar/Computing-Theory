#include <iostream> // Para poder usar cin y cout
#include <stdlib.h> //Aqui estan las funciones rand y srand
#include <time.h> // De aqui se usa la funcion time para obtener un indicador del tiempo actual del sistema para la semilla
#include <string.h>
#include <string> // Para trabajar con cadenas
#include <fstream> // Para poder trabajar con .txt
using namespace std;

string automata(string);

int main(){
	string cadena = "0110111101101010001010111110100010011000100100100011101001010110";
	cout << automata(cadena);
}
string automata(string cadena){
	int largo;
	largo = cadena.length();
	//declaracion de estados del automata
	int q0 = 0;
	int q1 = 1;
	int q2 = 2;
	int q3 = 3;
	int actual;
	actual = q0;
	
	bool fin = false;
	int conta = 0;
	//caracter
	char cr = ' ';
	while (fin == false){
		if(conta >= largo){
			fin == true;
			break;
		}	
		//estado q0 no aceptada	
		if (actual == q0) {
			if(cadena[conta] == '1'){
				actual = q1;
			}
			if(cadena[conta] == '0'){
				actual = q2;
			}
		}
		//estado q1 aceptada
		else if (actual == q1){
			if(cadena[conta] == '1'){
				actual = q0;
			}
			if(cadena[conta] == '0'){
				actual = q3;
			}
		}
		//estado q2 aceptada
		else if (actual == q2){
			if(cadena[conta] == '1'){
				actual = q3;
			}
			if(cadena[conta] == '0'){
				actual = q0;
			}
		}
		//estado q3 aceptada
		else if (actual == q3){
			if(cadena[conta] == '1'){
				actual = q2;
			}
			if(cadena[conta] == '0'){
				actual = q1;
			}
		}
		
		conta++;
	}	
	string estado = " ";
	
	if(actual == 0){
		estado = "rechazada";
	}
	else if( actual == 1 || actual == 2 || actual == 3){
		estado = "aceptada";
	}
	//cout << actual << endl;
	return estado;
}