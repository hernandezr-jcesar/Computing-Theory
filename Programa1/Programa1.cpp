/*
	Programa 1 -> Teoria de la Computacion
	Programa que calcula el universo del alfabeto binario
	hasta n
	
	S ^ n = s^0 U s^1 U s^2 U ... U s^n
	k= 0, 1, 2, ... n-1, n
	
	El alfabeto a usar es:
 	Sigma = {0,1}
 	
 	sigma ^ * = {(Todas las combinaciones posibles,
	de los elementos del alfabeto)}
	
	ENTRADA
	-> Un numero (Limite del programa ) entre 0 y 1000
	SALIDA
	<- Universo del alfabeto binario en un .txt
	 
	 NOTA : En el reporte en especial poner n=26
*/
#include <iostream> // Para poder usar cin y cout
#include <string.h> // Para trabajar con cadenas
#include <fstream> // Para poder trabajar con .txt
#include <cstdlib> //Aqui estan las funciones rand y srand
#include <ctime> // De aqui se usa la funcion time para 
//obtener un indicador del tiempo actual del sistema para 
//la semilla
using namespace std;

void menu();
void manualmente();
void automaticamente();
string Decimal_A_Binario(int);
int limitedeunos(int);
string llenar0(string,int);
void sigmaasterisco(int);
void ContadorDeUnosATexto();

int main (){
	menu();
	return 0;	
}

void menu(){
	int opcion = 0;
	
	do{
		system("cls"); 
		cout << "Programa que calcula el universo del alfabeto binario\n" << endl;
		cout << "Opciones:"<< endl;
		cout << "1.- Ingresar el valor de n manualmente." << endl;
		cout << "2.- Ingresar el valor de n automaticamente." << endl;
		cout << "3.- Salir." << endl;
		cin >> opcion;			
		
		switch (opcion) {
			case 1 :  
				system("cls");
				manualmente();
				system("pause");
			break;
			case 2 : 
				system("cls");
				automaticamente();
				system("pause");
			break;
			case 3:  opcion = 3; break;			
			default:
				system("cls");
				cout << "Favor de ingresar un valor valido" << endl;
				system("pause");
		}
	}while(opcion !=3);
	
}
void manualmente(){
	int numero;
	cout << "Manualmente" << endl;
	cout << "Favor de ingresar el valor de n :"<<endl;
	cin >> numero;
	sigmaasterisco(numero);	
	ContadorDeUnosATexto();//Se imprime las cantidades de 1 por cadena
}
void automaticamente(){
	int numero;
	srand(time(NULL));
	numero = rand() % 1001;//0 a 1000
	cout << "Automaticamente" << endl;
	cout << "El valor de n es:" << numero << endl;
	sigmaasterisco(numero);	
	ContadorDeUnosATexto();//Se imprime las cantidades de 1 por cadena		
}
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
/*
	(1)	1 -> 1
	(2) 11 -> 3
	(3) 111 -> 7
	(4) 1111 -> 15
	(5) 11111 -> 31
	(6) 111111 -> 63
*/
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
	
	fstream archivo;
	archivo.open("SigmaUniverso.txt",ios::out);
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
	archivo << "}.|";
	archivo.close();	
}

void ContadorDeUnosATexto(){
	cout << "Contando cantidad de 1 en cada cadena..." << endl;
	
	fstream archivo;
	archivo.open("SigmaUniverso.txt",ios::in);
	string linea;
	if (archivo.is_open()) 
	{
		fstream archivodeunos;
		archivodeunos.open("CantDeUnos.txt",ios::out);
		while(!archivo.eof())
		{	
			getline(archivo,linea);
			long long int conta = 1;
			int cantidadunos = 0;
			archivodeunos << "X" << endl;
			while((linea[conta]) != '|'){	
				if (linea[conta] == '1'){
					cantidadunos++;
				}
				if (linea[conta] == ',' ){					
					archivodeunos << cantidadunos << endl;
					cantidadunos = 0;		
				}	
				if (linea[conta] == '.' ){					
					archivodeunos << cantidadunos << endl;
					cantidadunos = 0;		
				}		
				conta++;
			}	
			//cout << conta << endl;
		}		
		archivodeunos.close();
	}
	archivo.close();
	
	cout << "Archivo Creado." << endl;
}


