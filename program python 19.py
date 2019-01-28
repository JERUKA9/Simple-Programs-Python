class Parent():
    
    def __init__(self):
        
        print("Parent init")
        
        def Parent(self):
            print("Parent parent")
            
            def Poke(self):
                print("Parent poked")
                
                class Child(Parent):
                    
                    def __init__(self):
                        
                        print("Child init")
                        
                        def Poke(self):
                            
                            print("Child poked")
                            
                            child = Child()
                            
                            child.Poke()
                            
                            child.Parent()