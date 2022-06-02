numDays = []
a=b=c=0

print("Enter the Number of days: ")
s = int(input())

print(end="Enter " +str(s)+ " days sales values: ")
for i in range(s):
  numDays.insert(i, int(input()))

for i in range(s):
  if numDays[i]>0:
    a +=1
  elif numDays[i]<0:
    b+=1
  else:
    c+=1

print(end="\nNumber of positive sales days : " +str(a))