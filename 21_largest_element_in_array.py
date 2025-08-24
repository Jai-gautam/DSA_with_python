nums = [1,2,12,2,3,-1,1000,0,5]
largest = float("-inf")
n = len(nums)

for i in range(0,n):
    largest = max(largest,nums[i])

print(largest)