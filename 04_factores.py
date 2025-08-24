from math import sqrt
num = int(input("enter a number"))
n = num
arr=[]
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        arr.append(i)
        x = num//i
        if(x!=i):
            arr.append(x)

print(arr)