# INSERTION SORT:


nums = [22,13,200,55]
 
def insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        if(nums[i]<nums[i-1]):
            key = nums[i]
            j = i-1
            while(nums[j]>key and j>=0):
                nums[j+1]=nums[j]
                j-=1
            
            nums[j+1] = key
        
             

    print(nums)

insertion_sort(nums)