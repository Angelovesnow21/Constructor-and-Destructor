class Employee:

    # Intializing (Constructor)
    def __init__(self):
        print("Employee created")
    def mym(self):
        print("I am my method")
    # Deleting (Destructor)
    def __del__(sef):
        print("Destructor called, Employee deleted")

obj = Employee()
obj.mym()