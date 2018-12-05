#include<iostream>
#include<cmath>

using namespace std;
int N = 100;
double lista[100];

void meter(double *x);

int main(){
    cout << "Here I am, ponqué" << endl;
    meter(lista);
    return 0;
}

void meter(double *x){
    FILE *f;
    f = fopen("datos.dat", "w");
    for (int i = 0 ; i<N ; i++){
        x[i] = sin(i*0.1) + cos(i*0.1);
        fprintf( f, "%f %f \n", i*1.0, x[i]);
    }
}