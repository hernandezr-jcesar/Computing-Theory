#include <iostream>
#include <math.h>
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
int suelo(int s){
	return (pow(2,s));
}
int main(){
	
	int limite=0;
	string binario="";
	
	cin >> limite;
	//int topeabajo=limite-1;
	int u = 1;
	//if limite == 0	
	
		for(int conta = 0; conta <= limitedeunos(limite);conta++){
	 		binario = Decimal_A_Binario(conta);
				
				cout << binario << endl;
			}
			
	
	
/*
	for(int i = 0;i< limite;i++){
		binario = "0" + binario;
		
	}
	for(int j = 0; j < pow(2,limite);j++){
			
			cout << binario << endl;
	}
	*/
	
	return 0;
}
/*
1->1			*
3->11  			*
7->111		
15->1111		*	
31->11111
63->111111
127->1111111
255->11111111	*

n= 2n +1
Creo que es mejor que hagas un programa que calculé las posibles combinaciones con 0 y 1 dependiendo del k


1->1
2->10
4->100
8->1000
16->10000
32->100000
*/
