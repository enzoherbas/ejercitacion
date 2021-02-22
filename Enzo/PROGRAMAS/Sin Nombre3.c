
//Insertar 3 numeros y que me muestre el mayor y el menor de los 3!

#include <stdio.h>

int main(){
	int x,y,z;
	int mayor, menor;
	
	printf("Introduce el primer valor\n");
	scanf("%i",&x);
	printf("Introduce el segundo valor\n");
	scanf("%i",&y);
	printf("Introduce el tercer valor\n");
	scanf("%i",&z);
	
	if (x > y){
		if (x > z){
			mayor = x;
		}
		else{
			mayor = z;
		}
	}
	else {
		if (y > z){
			mayor = y;
		}
		else{
			mayor = z;
		}
	}
	if (x < y){
		if (x < z){
			menor = x;
		}
		else{
			menor = z;
		}
	}
	else {
		if (y < z){
			menor = y;
		}
		else{
			menor = z;
		}
	}
	printf("El valor mas grande es %i\n",mayor);
	printf("Y el valor mas pequeño es %i\n",menor);
	system("pause");
	return 0;
}
