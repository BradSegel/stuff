#include <stdlib.h>
#include <stdio.h>

void getRange( char * prompt, int * lo, int * hi)
{
    do {
        printf("\nEnter floor Value%c", *prompt);
        scanf("%d", lo);
        printf("\nEnter Ceiling Value%c", *prompt);
        scanf("%d", hi);
    } while ( *lo >= *hi );
}

int main(){
    int a=0, b=0;
    char prompt= '>';

    getRange(&prompt, &a, &b);
    printf("Your range is from %d to %d\n",a,b);
    return 0;
}

