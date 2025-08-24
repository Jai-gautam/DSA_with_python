# BUBLE SORT : like buble in water , we select the largest and place it at last
#            : i iterates from last-1 index to 0 
#            : jniterates from j to i and compare and swap the elements

nums = [22,1,3,44,55,221,45]

def buble_sort(nums):
    n = len(nums)
    for i in range (n-2,-1,-1):
        swaping = False
        for j in range (0,i+1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swaping = True
        if(swaping == False):
            print(nums)
            return
        
    

buble_sort(nums)

#  TIME COMPLEXITY O(N**2)
# SPACE COMPLEXITY O(1)