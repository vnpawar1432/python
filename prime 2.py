num1 = int(input("enter the no: "))
prime = 0
if(num1>1):
    for i in range(2,num1):
            if(num1%i==0):
                prime = 1
                break
    if(prime == 0):
        print(f"{num1} is prime")
    else:
        print(f"{num1} is not prime")
