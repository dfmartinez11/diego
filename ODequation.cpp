#include<iostream>
#include<cmath>
using namespace std;

int N=300;
double x[3000];
double dt=0.01;

double derivada(double x);
void euler(double *x, double condicionI);

int main(){
    FILE *f;
    f = fopen("difSencilla.dat" ,"w");
    euler(x , 0.0);
    cout << "Pinche ponquesito" << endl;
    for(int i=0 ; i<N ;i++){
        fprintf(f , "%f %f \n", i*dt, x[i]);
    }
    fclose(f);
    return 0;
}

double derivada(double x){
    return cos(x);
}

void euler(double *x, double condicionI){
    x[0] = condicionI;
    for(int i=1 ; i<N ;i++){
        x[i] = x[i-1] + dt*( cos(x[i-1]) );
    }
}