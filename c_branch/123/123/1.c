#include <stdio.h>
#include <stdlib.h>
int main()
{ int a=3,b=5,c;
	c=(a>--b)?a++:b--;
	printf("%d%d\n",a,b);
	system("pause");
	return 0;
}