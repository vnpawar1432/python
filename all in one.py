#   #fabonica
# x,y = 0,1
# print(x)
# while y<50:
#     print(y)
#     x,y = y,x+y
#
# #fabnica 2
# n = int(input("Enter the range"))
# a = 0
# b = 1
# if(n==1):
#     print(n)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c =a+b
#         a = b
#         b = c
#         print(c)


        #find prime no

# n1 = int(input("enter the range"))
# for i in range(0,n1):
#     prime = 0
#     if(i>1):
#         for j in range(2,i):
#             if(i%j==0):
#                 prime = 1
#                 break
#     if(prime==0):
#         print(f"{i} is prime")

        # prime no

# num = int(input())
# prime = 0
# if(num>0):
#     for i in range(2,num):
#         if(num%i==0):
#             prime = 1
#             break
# if(prime==0):
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")

            #leap

# year= int(input("enter year"))
#
# if(year%400==0 and year%100==0):
#     print("year is leap ")
# elif(year%4==0 and year%100 !=0):
#     print("year is leap")
# else:
#     print("year is not leap")

        #sqrt
# num = int(input())
# sqrt = num**0.5
# print(sqrt)

    #sum of natural

# n= int(input())
# sum = n*(n+1)//2
# print(sum)

# find factorial

# num = int(input())
# factorial = 1
# if(num<0):
#     print("sorry NO factorial for -ve no")
# elif(num==0):
#     print("factorial of 0 is 1")
# elif(num>0):
#     for i in range(1,num+1):
#         factorial = factorial*i
#         print(factorial)

    #all vowels in string

# str =input()
# str = str.lower()
# vowels = ("aeiou")
# s = set({})
# for i in str:
#     if i in vowels:
#         s.add(i)
#     else:
#         pass
# if(len(vowels) == len(s)):
#     print("all vowelss in string")
# else:
#     print("not all vowelss in string")

    #Remove duplicate from string
# str = input("enter the string: ")
# t = ""
# for i in str:
#     if i in t:
#         pass
#     else:
#         t = t+i
# print(t)

    # Reverse the string
# str = input("enter the string: ")
# str1 = str.split(" ")
# str = " ".join(reversed(str1))
# print(str)

        # frequency
# str = input("enter the string: ")
# s={}
# for i in str:
#     if i in s:
#         s[i] +=1
#     else:
#         s[i] = 1
# for i in str:
#     if s[i] != 0:
#         print("{}{}".format(i,s[i]),end="")
#        s[i]=0