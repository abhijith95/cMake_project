from piTestCore import piTestCore
from piTestFactory import piTestFactory

class test_acts(piTestCore):
    
    operator_map = {"Add": 1, "Subtract":2, "Multiply":3, "Divide":4}
    
    def test_act01(self):
        # checking for addition
        number1 = 10.0
        number2 = 20.0
        self.set(number1=number1, number2=number2)
        # checking the value of "sum" variable before running the operation
        sum_before = self.get(operation=self.operator_map["Add"])
        diff_before = self.get(operation=self.operator_map["Subtract"])
        
        self.equal(sum_before, 0, text="The initial sum should be zero")
        self.runDll(operation=self.operator_map["Add"])
        sum_after = self.get(operation=self.operator_map["Add"])
        diff_after = self.get(operation=self.operator_map["Subtract"])
        self.equal(sum_after, number1*number2, text="The output has to be the sum")
        self.equal(diff_before, diff_after, text="The difference should not change")

test = piTestFactory()
test.load_and_run_tests(test_acts)