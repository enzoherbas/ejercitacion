#include <stdio.h>

int main () {
	
	int x;
	
	printf ("valor de 1 a 4:");
	scanf ("%i",&x);
	
	switch(x) {
		case 1: printf ("Lunes\n");break;
		case 2: printf ("Martes\n");break;
		case 3: printf ("Miercoles\n");break;
		case 4: printf ("Jueves\n");break;
		default: printf ("no es capo\n");break;
	}
	
	system ("pause");
	return 0;
 	}
