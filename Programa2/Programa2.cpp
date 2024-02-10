#include <iostream> // Para poder usar cin y cout
#include <stdlib.h> //Aqui estan las funciones rand y srand
#include <time.h> // De aqui se usa la funcion time para obtener un indicador del tiempo actual del sistema para la semilla
#include <string.h> // Para trabajar con cadenas
#include <string>
#include <fstream> // Para poder trabajar con .txt
#include <thread> // Para dormir al programa
#include <cstdio> //para eliminar .txt

#include<graphics.h> //Para poder graficar
#include<conio.h> // Para poder usar el getch()
using namespace std;

const int WIDTH = 1000;
const int HEIGHT = 800;

using std::this_thread::sleep_for;
using namespace std::chrono_literals;

void menu();
void grafo();
void protocolo();
int cincuentacincuenta();
string generarcadena();
void guardarNcadenas(int,int);
int automata(string);
void verificarcadenas(int);
void juntarcorridas(int);

int main(){
	remove("TodasLasCadenas.txt");
	remove("Aceptadas.txt");
	remove("Rechazadas.txt");
	
	menu();
	
	return 0;
}
void menu(){
	int opcion = 0;
	bool menu = false;
	do{
		system("cls"); 
		cout << "Programa que implementa un protocolo de seleccion de cadenas binarias de 64 bits\n" << endl;
		cout << "Opciones:"<< endl;
		cout << "1.- Ver el grafo del protocolo." << endl;
		cout << "2.- Iniciar el protocolo" << endl;
		cout << "3.- Salir." << endl;
		cin >> opcion;			
		
		switch (opcion) {
			case 1 :  
				system("cls");
				cout<< "Grafo del protocolo" << endl;
				grafo();
				
			break;
			case 2 : 
				system("cls");
				protocolo();
				system("pause");
			break;
			case 3:  menu =  true; break;			
			default:
				system("cls");
				cout << "Favor de ingresar un valor valido" << endl;
				system("pause");
		}
	}while(menu == false);
	
}

void protocolo(){
	bool fin = false;
	int contavuelta = 0;				
	while( fin == false){			
		cout << "El protocolo esta listo?"<<endl;
		if(cincuentacincuenta() == 1){
			contavuelta++;	
			cout<< "Si" <<endl;			
			cout << "Creando cadenas..." << endl;
			guardarNcadenas(1000000, contavuelta);
			
			cout << "Cadenas creadas..." << endl;
			//Se duerme por 1 segundos
			sleep_for(1000ms);
				
			cout << "Validando cadenas..." << endl;			
			verificarcadenas(contavuelta);
			
			cout << "Vefificacion completa." <<endl;				
			cout << endl;				
		}
		else if(cincuentacincuenta() == 0){
			cout<< "No" <<endl;
			cout << "Fin del programa."<<endl;
			fin = true;				
		}					 			
	}
	//cout << contavuelta;
	if(contavuelta>=1){
		juntarcorridas(contavuelta);		
	}
}
//Funcion que tiene el 50% de probabilidad de que salga 0 o 1
int cincuentacincuenta(){
	int numero;
	srand(time(NULL));	
	numero = rand() % 2;	
	return numero;
}
//Funcion para generar la cadena de 0 y 1 de 64 bits de largo
string generarcadena(){
	string cadena = "";
	int numero;
	int limite = 64;
	for(int conta = 1; conta <= limite; conta++){
		numero = rand() % 2;	
		cadena = cadena + to_string(numero);	
	}	
	return cadena;
}

//Funcion del automata de seleccion de imparidades
//regresa un string dependiendo si la cadena es aceptada o no
// aceptada  => cadena aceptada
// rechazada => cadena rechazada
int automata(string cadena){
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
	int estado ;
	
	if(actual == 0){
		//rechazada
		estado = 0;
	}
	else if( actual == 1 || actual == 2 || actual == 3){
		//aceptada
		estado = 1;
	}	
	return estado;
}
//Funcion para guardar las n cadenas en un .txt
void guardarNcadenas(int limite, int contavuelta){	
	
	string nombrearchivo;
	nombrearchivo = "TodasLasCadenas"+ to_string(contavuelta)+ ".txt";
		
	ofstream todascadenas(nombrearchivo);		
	string cadenagenerada;
	if(todascadenas.is_open()){
		
		for(int conta=0; conta < limite; conta++){
			cadenagenerada = generarcadena();
			todascadenas << cadenagenerada << endl;
		}		
		
	}	
	todascadenas.close();		
	
}
void verificarcadenas(int contavuelta){
		
	string nombrearchivo;
	nombrearchivo = "TodasLasCadenas"+ to_string(contavuelta)+ ".txt";
	string archivoaceptadas;
	archivoaceptadas = "Aceptadas"+ to_string(contavuelta)+ ".txt";
	string archivorechazadas;
	archivorechazadas = "Rechazadas"+ to_string(contavuelta)+ ".txt";	
	string linea;
	ifstream Cadenas(nombrearchivo);					
	ofstream aceptadas(archivoaceptadas);			
	ofstream rechazadas(archivorechazadas);	
	if(Cadenas.is_open()){											
		while(getline(Cadenas,linea)){									
			//Si es aceptada se guarda en Aceptadas.txt
			if(automata(linea) == 1){
				if(aceptadas.is_open()){
					aceptadas << linea << endl;
				}					
			}
			if(automata(linea) == 0){						
				if(rechazadas.is_open()){
					rechazadas << linea << endl;	
				}								
			}												
		}											
	}
	rechazadas.close();
	aceptadas.close();	
	Cadenas.close();	
}

void juntarcorridas(int contavuelta){
		
	string linea;	
		for(int i = 1; i <= contavuelta; i++){
			
			string nombrearchivo = "TodasLasCadenas"+ to_string(i)+ ".txt";			
			ifstream cadenas(nombrearchivo);
			fstream cadenasfinal("TodasLasCadenas.txt",ios::app);
			if(cadenas.is_open()){
				if(cadenasfinal.is_open()){
					cadenasfinal << "Vuelta: "<< i << endl;
					while(getline(cadenas,linea)){
						cadenasfinal << linea << endl;
					}
					cadenasfinal << endl;	
				}				
				cadenasfinal.close();
			}
			cadenas.close();
			char * archivotexto1 = new char[nombrearchivo.length() + 1];
			strcpy(archivotexto1, nombrearchivo.c_str());					
			remove(archivotexto1);
	
			string archivoaceptadas = "Aceptadas"+ to_string(i)+ ".txt";			
			ifstream aceptadas(archivoaceptadas);
			fstream aceptadasfinal("Aceptadas.txt",ios::app);
			if(aceptadas.is_open()){
				if(aceptadasfinal.is_open()){
					aceptadasfinal << "Vuelta: "<< i << endl;
					while(getline(aceptadas,linea)){
						aceptadasfinal << linea << endl;
					}
					aceptadasfinal << endl;	
				}				
				aceptadasfinal.close();
			}
			aceptadas.close();
			char * archivotexto2 = new char[archivoaceptadas.length() + 1];
			strcpy(archivotexto2, archivoaceptadas.c_str());					
			remove(archivotexto2);	
			
			string archivorechazadas = "Rechazadas"+ to_string(i)+ ".txt";			
			ifstream rechazadas(archivorechazadas);
			fstream rechazadasfinal("Rechazadas.txt",ios::app);
			if(rechazadas.is_open()){
				if(rechazadasfinal.is_open()){
					rechazadasfinal << "Vuelta: "<< i << endl;
					while(getline(rechazadas,linea)){
						rechazadasfinal << linea << endl;
					}
					rechazadasfinal << endl;	
				}				
				rechazadasfinal.close();
			}
			rechazadas.close();
			char * archivotexto3 = new char[archivorechazadas.length() + 1];
			strcpy(archivotexto3, archivorechazadas.c_str());					
			remove(archivotexto3);	
		}		
	
}
void grafo(){
	initwindow(WIDTH,HEIGHT,"Grafo de protocolo");
	setbkcolor(WHITE);
	cleardevice();
	setcolor(BLACK);
	setlinestyle(SOLID_LINE,0,3);
	
	setfillstyle(SOLID_FILL,BLACK);
	//Lineas
	//q0--q2
	line(100,150,100,630);
	circle(100,640,8);
	floodfill(102,640,BLACK);	
	//q0--q1
	line(160,110,850,110);
	circle(158,110,8);
	floodfill(158,110,BLACK);
	//q1--q3
	line(900,170,900,650);		
	circle(900,160,8);
	floodfill(900,160,BLACK);
	//q3--q2
	line(150,690,835,690);
	circle(843,690,8);
	floodfill(843,690,BLACK);

	settextstyle(8, 0, 6);
	//Q	
	circle(500,400,50);			
	outtextxy(480,370,"Q");	
	//->q
	setfillstyle(SOLID_FILL,BLACK);
	circle(500,460,8);
	floodfill(500,460,BLACK);
	//Inicio--Q
	line(500,470,500,500);
	//Inicio
	settextstyle(8, 0, 4);
	outtextxy(450,505,"Inicio");	
	
	// 0
	outtextxy(520,310,"0");		
	
	//OFF
	circle(500,250,50);			
	outtextxy(470,235,"OFF");
	//->OFF
	setfillstyle(SOLID_FILL,BLACK);
	circle(500,310,8);
	floodfill(500,310,BLACK);
	//Q--OFF
	line(500,310,500,350);
	
	settextstyle(8, 0, 5);
	//q0
	circle(100,100,50);		
	outtextxy(75,80,"q0");
	//q1
	circle(900,100,40);
	circle(900,100,50);
	outtextxy(875,80,"q1");
	//q2
	circle(100,700,40);
	circle(100,700,50);
	outtextxy(75,680,"q2");
	//q3
	circle(900,700,40);
	circle(900,700,50);
	outtextxy(875,680,"q3");
	
	
	//q -- q0
	line(145,145,462,362);
	//->q0
	setfillstyle(SOLID_FILL,BLACK);
	circle(142,140,8);
	floodfill(143,142,BLACK);
	
	settextstyle(8, 0, 4);
	//1
	outtextxy(350,250,"1");		
	
	//arco q0 -> q1
	arc(500,800,65,116,790);
	circle(842,90,8);
	floodfill(844,92,BLACK);
	
	//arco q2 -> q3
	arc(500,0,245,296,790);	
	circle(158,711,8);
	floodfill(158,711,BLACK);
		
	//arco q0 -> q2
	arc(800,400,161,200,790);
	circle(60,140,8);
	floodfill(60,140,BLACK);
	
	//arco q1 -> q3
	arc(200,400,341,20,790);	
	circle(945,660,8);
	floodfill(945,660,BLACK);
	
	// 0 y 1 externos
	settextstyle(8, 0, 4);
	outtextxy(150,40,"1");
		
	outtextxy(970,150,"0");
	
	outtextxy(800,750,"1");
	
	outtextxy(20,640,"1");
	
	// 0 y 1 internos
	outtextxy(70,200,"0");
		
	outtextxy(300,700,"1");
	
	outtextxy(920,550,"0");
	
	outtextxy(700,70,"1");
	
	system("pause");
	closegraph();
}