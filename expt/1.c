#include <stdio.h>
#include <stdlib.h>

int main(void) {
	FILE *fp;
	char fname[] = "0.jpg";
    int chr;

	fp = fopen(fname, "r");
	if(fp == NULL) {
		printf("%s を開けず\n", fname);
		return -1;
	}
 	while((chr = fgetc(fp)) != EOF) {
 		putchar(chr);
 	}

	fclose(fp);
	return 0;
}
