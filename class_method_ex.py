# getting the properties own instance's every properties requires self parametter
class TestClass:
    num = 0
    def __init__(self, num):
        self.num = num

    def test_method(self):
        print(f'test method invoked {self.num}')
        return self.num
        
    def test_method2(self):
        print(f'method 2 invoked {self.test_method}')
        
        
tc1 = TestClass(1)
tc1.test_method()