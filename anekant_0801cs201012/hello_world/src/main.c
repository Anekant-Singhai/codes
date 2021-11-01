#include <stdio.h>
#include "..\include\myfile.h"

int main(){

    char name[] = "Abhinav";
    sgs_clib_convert_to_upper(name);

    printf("After convering to all Caps name is: %s",name);
}