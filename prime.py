num1 = int(input("Enter the range: "))
for i in range (0,num1):
    prime = 0
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                prime = 1
                break
    if(prime==0):
        print(f"{i} is prime")