
/*
This is a header file to be used in the project
*/

extern const int TRUE;
extern const int FALSE;

/* creating answer variables to be used in the main file*/
static float sum=0.0;
static float diff=0.0;
static float product=0.0;
static float quotient=0.0;
static float number1=1.0;
static float number2=1.0;

extern void read(float num1, float num2);
extern void add(float *number1, float *number2);
extern void subtract(float *number1, float *number2);
extern void multiply(float *number1, float *number2);
extern void division(float *number1, float *number2);
extern void main_func();
extern int good_B(float *number);
