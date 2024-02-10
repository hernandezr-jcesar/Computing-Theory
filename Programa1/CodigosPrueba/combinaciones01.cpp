#include <iostream>
#include <math.h>
using namespace std;
//Programa que calcula las combinaciones posibles de 0 y 1 dado un k
int main(){
	int uno, cero;
	
	uno = 1;
	cero = 0;
	
	int k;
	
	cin >> k;
	string binario;
	
	for(int i = 0;i< k;i++){
		binario = "0" + binario;
		
	}
	for(int j = 0; j < pow(2,k);j++){
			
			cout << binario << endl;
	}
	
}
