#include <local_library.h>

const int TRUE = (int) 1;
const int FALSE = (int) 0;

void add(float *number1, float *number2)
{
	sum = *number1 + *number2;
}

void subtract(float *number1, float *number2)
{
	diff = *number1 - *number2;

}

void multiply(float *number1, float *number2)
{
	product = *number1 * *number2;
}

int good_B(float *number)
{

	if ( *number == FALSE )
	{
		return (FALSE);
	}
	
	else
	{
		return (TRUE);
	}

}

void division(float *number1, float *number2)
{
	int result1_b; 
	int result2_b;

	result1_b = good_B(number1);
	result2_b = good_B(number2);

	if ((result1_b == TRUE) && (result2_b == TRUE))
	{
		quotient = *number1 / *number2;
	}
	else
	{
		quotient = 0;
	}
	
}

void main_func()
{
	add(&number1, &number2);
	subtract(&number1, &number2);
	multiply(&number1, &number2);
	division(&number1, &number2);
}

void read(float num1, float num2)
{
	number1 = num1;
	number2 = num2;
}