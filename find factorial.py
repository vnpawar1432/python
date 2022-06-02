num = int(input())
fact = 1
if (num<0):
    print("no factoraial for -ve")
elif(num==0):
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(fact)