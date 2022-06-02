
class computer:
    comp = "Lenovo"
    r = 12
    
    def __init__(self,company,ram):     #constructor : to allocate the memory
        self.comp = company              # define variables
        self.r = ram
        # print("I am constructor")

    def hello(self):
        print("hello")
        print(self.comp,self.r)


    def hey(self):
        print("hey")
        print(self.comp,self.r)


obj1 = computer("dell",2048)# company, ram
obj1.hey()

obj2 = computer("hp",4096)
obj2.hey()

