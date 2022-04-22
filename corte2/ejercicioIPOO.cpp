#include <iostream>
using namespace std;

int main(){
    cout << "Ingrese el # de filas" << endl;
    cout << "Ingrese el # de columnas" << endl;

    int m,n;
    cin >> n;
    cin >> m;

    int A[n][m];
    for(int k=0;k<=n/2;k++){
        for(int i=k; i<n-k; i++){
            for(int j=k; j<m-k; j++){
                A[i][j] = k+1;
            }
        }
    }
    

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout << A[i][j] << " ";
        }
        cout << endl;
    }

}