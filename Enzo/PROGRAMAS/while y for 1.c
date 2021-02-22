#include <stdio.h>

int main () {
	int x, y, i;
	
	printf ("Dame un valor:");
	
	scanf ("%i",&x);
	
	printf ("Dame otro valor, mayor al anterior:");
	
	scanf ("%i",&y);
	
	printf ("\n");
	
	
	for (i = x + 1 ; i < y ; i++){
		printf ("%i,",i);}
	
	i = x + 1;
		printf ("\n");
		
	while (i < y) {
		printf ("%i, ", i);
		i++;
	}
	
	
	 
	printf ("\n");
	system ("pause");
	return 0;
}
