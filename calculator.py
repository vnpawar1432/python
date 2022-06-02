num1 = int(input())
num2= int(input())
opr =input("enter a for add, s for sub : ")
while True:
    def add(num1,num2):
        total = num1+num2
        return total
    def sub(num1,num2):
        total = num1-num2
        return total
    add(num1,num2)
    sub(num1,num2)
    if(opr=='a'):
        print(add(num1,num2))
    elif(opr=='s'):
        print(sub(num1,num2))
    else:
        print("invalide char")
    break