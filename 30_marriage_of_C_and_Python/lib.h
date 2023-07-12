/*	for function prototypes */

#ifndef LIB_H
#define LIB_H

/// @brief	Prints 'Hello', which will be in use for python.
void sayHelloFromC(void);

/// @brief Square multiplication for an array of numbers.
/// @param n number of elements to use
/// @param array_in input array with n elements
/// @param array_out result array of n elements
void squareMultiplication(int n, double *array_in, double *array_out);

#endif