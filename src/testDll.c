#include <local_library.h>
/*
Note that __declspec(dllexport) in front of every function is required if needed to be accessed in python.
Else python will complain "Function not found in dll file"
*/
#define DLLEXPORT __declspec(dllexport)
// struct output_variable
// {
// 	float sum;
// 	float diff;
// 	float product;
// 	float quotient;
// };
/* function that gets input from outside */
DLLEXPORT void setNumbers(float num1, float num2)
{
	number1 = num1;
	number2 = num2;
}

DLLEXPORT void runTest(int operation)
/*operation (int):
	1 - for addition
	2 - for subtraction
	3 - for multiplication
	4 - for division*/
{
	switch (operation)
	{
	case 1:
		add(&number1, &number2);
		break;
	case 2:
		subtract(&number1, &number2);
		break;
	case 3:
		multiply(&number1, &number2);
		break;
	case 4:
		division(&number1, &number2);
		break;
	default:
		break;
	}
}

DLLEXPORT float getNumbers(int operation)
{
	switch (operation)
	{
	case 1:
		return sum;
		break;
	case 2:
		return diff;
		break;
	case 3:
		return product;
		break;
	case 4:
		return quotient;
		break;
	default:
		return 0.0;
		break;
	}

}