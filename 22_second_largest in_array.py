nums = [1,33,22,22,99,-100,0,1,-1,1000]

def second_largest(nums):
    n = len(nums)
    largest = float("-inf")
    sec_lar = float("-inf")
    for i in range (0,n):
        if (nums[i]>largest):
            sec_lar = largest
            largest = nums[i]

    return sec_lar

result = second_largest(nums)
print(result)