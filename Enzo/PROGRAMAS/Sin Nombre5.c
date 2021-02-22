//Bloque ay nose

#include <stdio.h>

int main () {
	int x, y, aux;
	
	printf ("El valor de x es:");
	scanf ("%i",&x);
	
	printf ("El valor de y es:");
	scanf ("%i",&y)	;
	
	aux= x;
	x = y;
	y = aux;
	
	printf("El valor de x es: %i\n",x);
	printf("El valor de y es: %i\n",y);
	
	system ("pause");
	return 0;
	
}
