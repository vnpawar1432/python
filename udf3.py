# calculator

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
oper = input("a for add, s for sub,m for mul,d for div:  ")

def add():
    total = num1+num2
    print(total)

def sub():
    total = num1-num2
    print(total)

def mul():
    total = num1*num2
    print(total)

def div():
    total = num1/num2
    print(total)

if(oper == "a"):
    add()
if(oper == "s"):
    sub()
if(oper == "m"):
    mul()
if(oper == "d"):
    div()