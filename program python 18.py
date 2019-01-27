from timeit import dummy_src_name

class Calculator():
    def __init__(self):
        self.last_result = 0
        
    def add(self,a,b):
        
        result=a+b
        self.last_result = result
        print(result)
        
        def substract(self,a,b):
            result=a-b
            print(result)
            calc2 = Calculator()
            
            calc2.add(5,3)
            print(calc2.last_result)
            