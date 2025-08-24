num = int(input("enter a number"))
n = num
sum = 0
while(n>0):
    x = n%10
    sum = sum + x**3
    n = n//10

print(sum == num)