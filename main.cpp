#include <iostream>

using namespace std;

int main()
{
    int vetor [80];
    cout << "Digite 8 numeros para o vetor: " << endl;
    for (int i = 0; i < 8; i++)
    {
        cout <<"Numero " << i + 1 << ";";
        cin >> vetor [i];
    }

    cout << "\nVetor inserido: ";
    for (int i = 0; i < 8; i++)
    {
        cout << vetor [i] << " ";
    }
    cout << endl;

    //Convertendo para matriz 3D
    int matriz3D [2] [2] [2];
    int index = 0;
    for (int i =0; i < 2; i++)
    {
        for (int j =0; j < 2; j++)
        {
          for (int k = 0; k < 2; k++)
          {
            matriz3D [i] [j] [k] = vetor[index++];
          }  
        }
    }

    //Exibindo a matriz
    cout << "\nMatriz 3D (2x2x2);\n";
    for(int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                cout << "matriz3D["<< i <<"][" << j << "][" << k << "] = " << matriz3D [i] [j] [k] << endl;
            }     
        }
    }
    return 0;       
}