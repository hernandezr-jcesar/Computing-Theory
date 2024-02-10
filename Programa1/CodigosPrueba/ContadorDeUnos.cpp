#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;


int main(){
	
	cout << "Contador de Unos" << endl<< endl;
	/*
	cout << "Ingrese la cantidad n con la que se genero el archivo"<< endl;
	int n;
	cin >> n;
	
	int limite =(limitedeunos(n));
	*/
	//string nombrearchivo = "PruebasDeTexto.txt";
	
	
	ifstream archivo("PruebasDeTexto.txt");
	//char linea[200];
	string linea;
	if(archivo.fail()){
		cerr << "Error al abrir el archivo" << endl;
	}
	else{
		while(!archivo.eof()){
				
			getline(archivo,linea);
			
			int conta = 1;
			int cantidadunos = 0;
			int renglon = 0;
			while((linea[conta]) != '.'){
					
				if (linea[conta] == '1'){
					cantidadunos++;
				}
				if (linea[conta] == ',' || linea[conta] == '}'){
					renglon++;
					cout << renglon<<"	"<< cantidadunos << endl;
					cantidadunos = 0;	
				}
				conta++;
			
			}
			cout << endl;
			//cout << linea << endl;						
			
		}
	}
	archivo.close();
	return 0;
}
