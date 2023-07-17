#include <stdio.h>
#include <stdlib.h>

int main()
{
    int year, age;

    printf("Please enter your date of birth: ");
    scanf("%d", &year);

    age = 2023 - year;

    printf("You are %d years old.", age);

    return 0;
}
