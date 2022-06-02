num = int(input())
prime = 0
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            prime = 1
            break
if(prime==0):
    print("no is prime")
else:
    print("no is not prime")