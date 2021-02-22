#include <stdio.h>

int main (){
	
	int x, y ,z;
	
	int max, min;
	
	printf ("Introduce el valor para x:");
	scanf ("%i",&x);
	
	printf ("Introduce el valor para y:");
	scanf ("%i",&y);
	
	printf ("Introduce el valor para z:");
	scanf ("%i",&z);
	
	if (x > y){
	if (x > z){
	max = x;
	}
	else {
	max = z;
	}
	}
	else{
	if (y > z){
	max = y;
	}
	else {max = z;}
	};
	

	printf("El mayor de los 3 numeros es: %i\n",max);
				
	if (max > x){
	if (y > x){
	min = x;	
	}
	else {
	min = y;
	}
	}
	else {
	if (x > z){
	min = z;
	}
	};
	printf ("El menor numero de los 3 es: %i\n",min);
			
	
	

	
	system ("pause");
	return 0;

}
