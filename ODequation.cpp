#include<iostream>
#include<cmath>
using namespace std;

int N=300;
double x[3000];
double t[3000];
double dt=0.01;

double derivada(double x);
void euler(double *x, double condicionI);
void runge(double *x, double condicionI);
void leapf(double *x, double cond);

int main(){
    FILE *f;
    f = fopen("difSencilla.dat" ,"w");
    euler(x , 0.0);
    cout << "Pinche ponquesito" << endl;
    for(int i=0 ; i<N ;i++){
        fprintf(f , "%f %f \n", i*dt, x[i]);
    }
    fclose(f);
    
    FILE *f2;
    f2 = fopen("difSencillaRunge.dat" ,"w");
    runge(x , 0.0);
    cout << "Pinche ponquesito" << endl;
    for(int i=0 ; i<N ;i++){
        fprintf(f2 , "%f %f \n", i*dt, x[i]);
    }
    fclose(f2);
    
    FILE *f3;
    f3 = fopen("difSencillaLeapF.dat" ,"w");
    leapf(x , 0.0);
    cout << "Pinche ponquesito" << endl;
    for(int i=0 ; i<N ;i++){
        fprintf(f3 , "%f %f \n", i*dt, x[i]);
    }
    fclose(f3);
    return 0;
}

double derivada(double x){
    return cos(x);
}

void euler(double *x, double condicionI){
    x[0] = condicionI;
    t[0] = 0.0;
    for(int i=1 ; i<N ;i++){
        x[i] = x[i-1] + dt*( cos(t[i-1]) );
    }
}

void runge(double *x, double condicionI){
    x[0] = condicionI;
    t[0] = 0.0;
    for(int i=1 ; i<N ;i++){
        double k1 = dt*( cos(t[i-1]) );
        double k2 = dt*( cos(t[i-1]) + (0.5*k1)  );
        x[i] = x[i-1] + k2;
    }
}

void leapf(double *x , double cond){
    x[0] = cond;
    t[0] = 0.0;
    for(int i=2 ; i<N ; i++){
        t[i] = t[i-1] + dt;
        x[i] = x[i-2] + ( 2*dt*cos(t[i-1]) );
    }
    
}