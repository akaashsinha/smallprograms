#include <stdio.h> 
#include <cs50.h>

int main(void)
{
    // asks for degrees in f
    printf("Temp in Fahreinheit: ");
    float f = GetFloat();
    
    // converts from f to c 
    float c = (5 / 9.0) * (f - 32);
    
    // display result
    printf("That number in C is %f\n", c);
    
    return 0;
}    
