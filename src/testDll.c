#include <local_library.h>

/* function that gets input from outside */
void setNumbers(float num1, float num2)
{
	number1 = num1;
	number2 = num2;
}

void runTest(int operation)
/*operation (int):
	1 - for addition
	2 - for subtraction
	3 - for multiplication
	4 - for division*/
{
	switch (operation)
	{
	case 1:
		add(&number1, &number2);;
		break;
	case 2:
		subtract(&number1, &number2);;
		break;
	case 3:
		multiply(&number1, &number2);;
		break;
	case 4:
		division(&number1, &number2);;
		break;
	default:
		break;
	}
}