#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main (){
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
			while((linea[conta]) != '.'){	
				if (linea[conta] == '1'){
					cantidadunos++;
				}
				if (linea[conta] == ',' ){					
					archivodeunos << cantidadunos << endl;
					cantidadunos = 0;	
				}				
				conta++;
			}	
			cout << conta << endl;
		}		
		archivodeunos.close();
	}
	archivo.close();
	
	cout << "Archivo Creado." << endl;;
	
	return 0;
	
}


