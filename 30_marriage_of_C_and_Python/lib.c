#include <stdio.h>
#include <stdlib.h>
#include "lib.h"

/// @brief	Prints 'Hello', which will be in use for python.
void sayHelloFromC(void) {
	puts("If you can read this text, then the library has sucessfully been loaded!");
	puts("By the way, Hello!");
}

/// @brief Square multiplication for an array of numbers.
/// @param n number of elements to use
/// @param array_in input array with n elements
/// @param array_out result array of n elements
void squareMultiplication(int n, double *array_in, double *array_out) {
	for(int i = 0; i < n; i++) {
		array_out[i] = array_in[i] * array_in[i];
	}
}