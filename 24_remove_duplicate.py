nums = [1,1,1,4,4,4,4,6,6,6,6,8,8,8,8,9,9,9,10,11]

def remove_duplicate(nums):
    n = len(nums)
    i = 0
    j = 1

    for j in range (1,n):
        if (nums[j]!=nums[i]):
            i+=1
            nums[i] = nums[j]
    
    return i+1

result = remove_duplicate(nums)
print(nums[0:result]) 

# TC O(N)
# SC O(1)