num = int(input("enter a number"))
n = num
x = 0
result = 0
while(n>0):
   x = n%10
   result = result*10 + x
   n = n//10

print(num == result)
   

