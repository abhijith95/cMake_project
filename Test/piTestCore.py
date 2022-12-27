import unittest
import ctypes
import os
import sys

class piTestCore(unittest.TestCase):   
    """
    This class focuses on running pyTest.dll in out/emul/Debug folder. There are functions that will set the two
    numbers, perform one of the four mathematical operations and can get the value of the performed operation.
    """ 
    
    dllObject = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), r'../out/emul/Debug/pyTest.dll'))
    result = {1:0, 2:0, 3:0, 4:0}
    nr_of_tests = 0
    nr_of_failed_tests = 0
    failed_messages = []
    tracebacks = []
    
    @staticmethod
    def check_operation_validity(operation):
        if operation not in (1,2,3,4):
            raise ValueError("Input value cannot be found in (1,2,3,4). Invalid input value")
    
    def set(self, number1, number2):
        """Function that sets value to two numbers

        Args:
            number1 (float): 
            number2 (float): 

        Raises:
            ValueError: If the input numbers are not float
        """
        if (not type(number1) == float) and (not type(number2) == float):
            raise ValueError("Entered argument is not of type float")
        else:
            self.dllObject.setNumbers(ctypes.c_float(number1), ctypes.c_float(number2))
    
    def get(self, operation):
        """Function that will retrieve the result for the operation

        Args:
            operation (int): {1: sum, 2:difference, 3:product, 4:quotient}
        """
        self.check_operation_validity(operation)
        # we need to tell python what is the return type of the function. If we don't specify this then python
        # does not accept the returned value.
        getNumbersObject = self.dllObject.getNumbers
        getNumbersObject.restype = ctypes.c_float
        self.result[operation] = getNumbersObject(operation)
        return getNumbersObject(operation)
    
    def runDll(self, operation):
        """Function that will retrieve the result for the operation

        Args:
            operation (int): {1: addition, 2:subtraction, 3:multiplication, 4:division}
        """
        self.check_operation_validity(operation)
        self.dllObject.runTest(operation)
    
    def equal(self, first, second, text):
        """Function that checks equality of two variables. If they are not equal it will print an error message.

        Args:
            first (): value of the first variable
            second (): value of the second variable
            text (string): text message to display if first != second
        """
        self.nr_of_tests+=1        
        try:
            self.assertEqual(first=first, second=second, msg=text)
        except self.failureException:
            self.nr_of_failed_tests+=1
            self.failed_messages.append(text)
            self.tracebacks.append(sys.exc_info())
    
    def notEqual(self, first, second, text):
        """Function that checks non-equality of two variables. If they are equal it will print an error message.

        Args:
            first (): value of the first variable
            second (): value of the second variable
            text (string): text message to display if first == second
        """
        self.nr_of_tests+=1        
        try:
            self.assertNotEqual(first=first, second=second, msg=text)
        except self.failureException:
            self.nr_of_failed_tests+=1
            self.failed_messages.append(text)
            self.tracebacks.append(sys.exc_info())