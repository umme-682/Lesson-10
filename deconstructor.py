class Employee:
    # Intializing (Constructor)
    def __init__ (self):
            print('Employee created.')
    
    # Deleting (Deconstructor)
    def __del__ (self):
            print('Destructor called, Employee deleted.')
            
obj = Employee()
del obj