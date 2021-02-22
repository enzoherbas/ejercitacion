#include <stdio.h>

int main () {
	
	int x , y , z, f;
	f = 0;
	printf ("Dame la hora en formato de 0 a 23\n");
	scanf ("%i",&x);
	printf ("Dame los minutos en formato de 0 a 59\n");
	scanf ("%i",&y);
	printf ("Dame los segundos en formato de 0 a 59\n");
	scanf ("%i",&z);
	
	if (z>=0 && z<=59 && y>=0 && y<=59 && x>=0 && x<=23)
	{z++;
	
	if (z>=0 && z<=59);
	else{;{y++;}{z=0;}}
	
	if (y>=0 && y<=59);
	else {{x++;}{y=0;};}
	
	if (x>=0 && x<=23);
	else {(x=24);{x=0;}};
	
	printf ("La hora es %i horas; ",x);
	printf ("%i minutos; ",y);
	printf ("%i segundos.",z);
}
	else printf ("Valores equivocados\n");
	
	system ("pause");
	return 0;
}
