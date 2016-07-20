#include <stdlib.h>
#include <stdio.h>

int is_palindrome( char * s ){

    // set pointer to the last char of string
    char *end = s;
    while (*end != '\0'){ end++; }
    // back off the terminal null
    end--;
    while (s++ <= end-- && *s == *end){;}

return s >= end;
}

int main(){
    printf("babaabab: %d\n", is_palindrome("babaabab"));   
    printf("racecar: %d\n",is_palindrome("racecar"));
    printf("Was it Eliot's toilet I saw?: %d\n",is_palindrome("wasiteliotstoiletisaw"));
    printf("gurny: %d\n",is_palindrome("gurny"));
    printf("empty string: %d\n", is_palindrome(""));
    printf("ad-hoc: %d\n", is_palindrome("abbg"));
}

