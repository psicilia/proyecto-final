/*
NAME 
   4-SiciliaPablo-MinCuad.c

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que aproxima una ecuacion al conjunto de puntos
    por el metodo numerico de minimos cuadrados

CATEGORY
    metodos numericos
    aproximacion funcional

USAGE
  4-SiciliaPablo-MinCuad.exe

GITHUB


*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int menu();
float sumatoria(int Vec_size, float *vector);
float power_sum(int Vec_size, float *vector, int power);
void free_vector(float *vector_limpio);
void free_matrix(float **matrix, int Matrix_size);
void print_Matrix(int l, float **matrix, float *results);

int main() {
  int C_puntos, Potencia_Max;
  int i, j, k, l, count;
  float **matriz, **datos;
  float temp, sumY, *results=NULL;
  printf("Bienvenido al metodo de minimos cuadrados \n");
  int MENU = 0;
  do{
    count = 1;
      if(MENU != 2){
        //leemos la cantidad de puntos
        printf("ingrese la cantidad de puntos: ");
        scanf("%d", &C_puntos);

        // reservamos la memoria para los puntos 
        datos = (float**)calloc(2, sizeof(float*));
        datos[0] = (float*)calloc(C_puntos, sizeof(float));
        datos[1] = (float*)calloc(C_puntos, sizeof(float));

        // leemos la potencia del polinomio
        printf("En que grado desea su polinomio: ");
        scanf("%d", &Potencia_Max);

        // leemos los puntos
        for(i=0; i<C_puntos; i++){

            printf("Ingrese el valor de X%d: ", i+1);
            scanf("%f", &datos[0][i]);

            printf("Ingrese el valor de Y%d: ", i+1);
            scanf("%f", &datos[1][i]);

        }
      }
      else{
        printf("En que grado desea su polinomio: ");
        scanf("%d", &Potencia_Max);
        free_vector(results);
      }

    // reservamos memoria para la matriz
    matriz = (float**)calloc(Potencia_Max+1, sizeof(float*));
    for (i = 0; i <= Potencia_Max; i++) {
      matriz[i] = (float*)calloc(Potencia_Max+1, sizeof(float));
    }
    // reservamos memoria para el vector de resultados
    results = (float*)calloc(Potencia_Max+1, sizeof(float));

    // generamos el sistema de ecuaciones
    for(i=0; i<=Potencia_Max; i++){  
      for(j = i; j <= (Potencia_Max+i); j++){ 
        if(!i && !j)
          matriz[0][0] = C_puntos;
        else
          matriz[i][j-i] = power_sum(C_puntos, datos[0], j);
      }
      sumY = 0;
      for(j = 0; j < C_puntos; j++)
        sumY += pow((datos[0][j]),i) * (datos[1][j]);
      results[i] = (i == 0) ? sumatoria(C_puntos, datos[1]) : sumY;
    }
    // imprimomos el sistema de ecuaciones
    printf("sistema de ecuaciones: \n");
    print_Matrix(Potencia_Max, matriz, results);

    //solucion por Gauss-jordan
    for (i = 0; i <= Potencia_Max; i++){
      temp = matriz[i][i];
      for (j = 0; j <= Potencia_Max; j++){
        matriz[i][j] = matriz[i][j] / temp;
      }
      results[i] = results[i] / temp;

      for (j = i+1; j <= Potencia_Max; j++){
        temp = matriz[j][i];
        for(k = 0; k <= Potencia_Max; k++){
          matriz[j][k] = matriz[j][k] - matriz[i][k] * temp;
        }
        results[j] = results[j] - results[i] * temp;
      }
    }
    print_Matrix(Potencia_Max, matriz, results);
    // Solucionamos la diagonal 
    for(i=0; i < Potencia_Max; i++){ 
      for(j=0; j <= ((Potencia_Max - 1) - i); j++){
        temp = matriz[j][j+count];
        for(k = j + count; k <= Potencia_Max; k++)
            matriz[j][k] -= (matriz[j+count][k] * temp);
        results[j] -= (results[j+count] * temp);  
      }
      count++;
    }
    //imprimimos la matriz resuelta
    printf("La matriz resuelta es: \n");
    print_Matrix(Potencia_Max, matriz, results);
    printf("el polinomio de grado %d es: \n", Potencia_Max);
    printf("Y = ");
    for (i = 0; i <= Potencia_Max; i++){
        if(i < 2){
          if(i == 0)
            printf("%f ", results[i]);
          else{
            if (results[i] < 0) printf(" %fx ", results[i]);
            else printf("+ %fx ", results[i]);
          }
        }
        else{
          if (results[i] < 0) printf(" %fx^%d", results[i],i);
          else printf("+ %fx^%d", results[i],i);
        }  
    }
    printf("\n");
    //LIBERACION DE MEMORIA 
    MENU = menu();

    if(MENU == 0){
      free_matrix(datos, 2);
      free_vector(results);
      free_matrix(matriz, Potencia_Max);
    }
  }while (MENU);
  
  return 0;
}

int menu(){
    int MENU;
    printf("para ingresar puntos nuevos ingrese 1\n");
    printf("para buscar una nueva ecuacion con los mismos puntos ingrese 2\n");
    printf("para salir ingrese 0\n");
    scanf("%d", &MENU);
    return MENU;
}

float sumatoria(int Vec_size, float *vector){
  float sum = 0;
  for(int i=0; i<Vec_size; i++)
      sum += vector[i];
  return sum;
}
float power_sum(int Vec_size, float *vector, int power){
      
  float result = 0;
  for(int i=0; i<Vec_size; i++)
    result += pow(vector[i],power);
  return result;
}

// Liberamos la matriz cuando sea necesario 
void free_matrix(float **matrix, int Matrix_size){
  if(matrix){
    for (int i = 0; i <= Matrix_size; i++)
      if(*(matrix+i)){
        free(*(matrix+i));
        *(matrix+i) = NULL;
      }
    free(matrix);
    matrix = NULL;
  }
}

// Se limpian los punteros a vector
void free_vector(float *vector_limpio){
  free(vector_limpio);
  vector_limpio = NULL;
}

// Se imprime la matriz y sus valores en Y
void print_Matrix(int l, float **matrix, float *results){
  printf("\n");
  for (int i = 0; i <=l; i++) {
    for (int j = 0; j <=l; j++)
      printf("%f\t", matrix[i][j]);
    printf("|\t%f\n", results[i]);
  }
}