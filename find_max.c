#include <stdio.h>

int main() {
    int n, i;
    float num, max;
    
    // Get the number of inputs from user
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    // Check if n is valid
    if (n <= 0) {
        printf("Please enter a positive number of elements.\n");
        return 1;
    }
    
    // Get the first number
    printf("Enter number 1: ");
    scanf("%f", &num);
    max = num; // Initialize max with the first number
    
    // Get remaining numbers and find maximum
    for (i = 2; i <= n; i++) {
        printf("Enter number %d: ", i);
        scanf("%f", &num);
        
        if (num > max) {
            max = num;
        }
    }
    
    // Display the result
    printf("\nThe maximum number is: %.2f\n", max);
    
    return 0;
}