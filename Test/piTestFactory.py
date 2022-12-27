import unittest
import sys

class piTestFactory:
    
    _test_suite = None
    _test_loader = unittest.TestLoader()
    _test_runner = unittest.TextTestRunner()
    
    def load_and_run_tests(self, testclass):
        self.load_tests(testclass)
        self.run_tests()
        self.print_result(testclass)
    
    def load_tests(self, testclass):
        self._test_suite = self._test_loader.loadTestsFromTestCase(testclass)
    
    def run_tests(self):
        self._test_runner.run(self._test_suite)
    
    def print_result(self, testclass):
        
        for index in range(testclass.nr_of_failed_tests):
            print(str(testclass.tracebacks[index]), file=sys.stderr)
            print("\n")
            print(testclass.failed_messages[index])
            print("\n")