# super() method is used to call parent class constructor from child class

class A:
    def __init__(self):
        print("Vaibhav")
    def Show(self):
        print("Parent class constructor ")

class B(A):
    def __init__(self):
        super().__init__()      # This is used to call parent class constructor
        print("pawar")
    def disp(self):
        print("child class constructor ")

obj = B()

obj.disp()
obj.Show()


