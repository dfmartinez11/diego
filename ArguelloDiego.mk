
###### Generar la figura Aleatorios.png
Armonico con Euler.png: graficasArmonico.py PosicionArmonicoEuler.txt

	python graficasArmonico.py 

Armonico con Euler.png: graficasArmonico.py PosicionArmonicoEuler.txt

	python graficasArmonico.py 

####### Ejecutar a.out
output.txt: a.out datos.cpp

	g++ datos.cpp -o a.out
	./a.out 

###### Abrir la figura
mostrar: 
	display Aleatorios.png

###### Borrar todos los archivos
clean:
	rm output.txt
	rm Aleatorios.png
	

#int main(){
#	//Aqui debe generar un archivo para escribir en el
#	ofstream fi("output.txt");
#	//------------------------------------------
#	int N,i;
#	cout<< "De un valor de N"<< endl;
#	cin >> N;
#	srand(time(0));
#	//Aqui debe imprimir en el archivo los datos random
#	for(i=0; i<N;i++){ 
#		fi << i << " " << rand()%N  << endl; 
#	}
#	//Aqui debe cerrar el archivo
#	fi.close();

#return 0;
#}
 



