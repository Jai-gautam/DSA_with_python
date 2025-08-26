# RIGHT ROTATE THE ARRAY BY 1 PLACE

nums = [1,2,3,4,5,6,7,8,9,10]
nums2 = [9,8,7,6,5,4,3,2,1]

def rra_slicing(nums):
    n = len(nums)
    nums[:] = nums[-1] + nums[0:-1]
    print(nums)



def rra(nums):
    n = len(nums2)
    temp = nums2[n-1]
    for i in range(n-2,-1,-1):
        nums2[i+1] = nums2[i]

    nums2[0] = temp

    print(nums2)


rra_slicing(nums)
rra(nums2)
