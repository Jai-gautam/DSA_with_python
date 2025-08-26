nums = [11,22,33,40,55,65,75,90,10000]

def check(nums):
    n = len(nums)
    if nums[0]<nums[1]:
        for i in range(1,n-1):
            if nums[i]>nums[i+1]:
                return False
        return True
    else:
        for i in range(2,n):
            if nums[i]>nums[i-1]:
                return False

        return True

result = check(nums)
print(result)       
            