#include <stdio.h>
#include <stdlib.h>
int main()
{
	int i;
	for (i=1;i<=4;i++)
	{
		if(((i!=1)+(i==3)+(i==4)+(i!=4)==3))
			printf("%d",i);
	}	
	system("pause");
	return 0;
}