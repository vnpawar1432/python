def Print():
    yield 1
    yield 2


p = Print()
print(p.__next__())
print(p.__next__())

a = range(1,10)
print(type(a))

for i in range(0,10):
    print(i)

# a =10
# b = 11.12
# print(type(a))


class Employee:
    def __init__(self,name,sal,role):
        self.name = name
        self.sal = sal
        self.role = role

    def printDetails(self,a,b,c):
        print(f"Name is {self.name},salary is {self.sal} and role is {self.role}")

emp1 = Employee("vaibhav",25000,"Associat I")
emp2 =Employee("vishal",36520,"Analyst")
print(emp1.name)
print(emp1.sal)
print(emp1.role)
print(emp2.printDetails())


