#include<iostream>
using namespace std;

double X[100];
double V[100];
int i;
void seudoEuler(double x0 , double v0 , double h, double *X[], double *Y[]);

// main
int main()
{
	double X[100];
	double V[100];
	seudoEuler(0.0 , 1.0 , 0.01 , X, V);
	//for (i=0 ; i<100 ; i++){
	//cout << X[i] << endl;
	//}
	cout << X[5] << endl;
	return 0;
}

void seudoEuler( double x00 , double v00 , double h, double *X[] ,double*V[])
{
		
	double x0 = x00;
	double v0 = v00;
	for(i=0 ; i<100 ; i++){
		double x = x0 + (i*h*v0);
		double v = v0 - (x0 * h);
		X[i] = x;
		V[i] = v;
		x0 = x;
		v0 = v;
	}
}
