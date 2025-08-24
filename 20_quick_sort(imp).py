# QUICK SORT :

def partition(nums,low,high):

    pivot = nums[low]
    i = low+1
    j = high

    while(i<j):
        while(nums[i]<=pivot):
            i+=1

        while(nums[j]>pivot):
            j-=1

        if(i<j):
            nums[i],nums[j] = nums[j],nums[i]
        else:
            break

    nums[j],nums[low] = nums[low],nums[j]

    return j

def quick_sort(nums,low,high):
    if(low<high):
        s = partition(nums,low,high)
        quick_sort(nums,low,s-1)
        quick_sort(nums,s+1,high)

    

nums = [7,4,10,1,6]
quick_sort(nums,0,4)

def partition(nums,low,high):


    pivot = nums[low]
    i = low+1
    j = high

    while(i<j):
        while(nums[i]<=pivot):
            i+=1

        while(nums[j]>pivot):
            j-=1
            
        if(i<j):
            nums[i],nums[j] = nums[j],nums[i]
        else:
            break

    nums[j],nums[low] = nums[low],nums[j]

    return j

def quick_sort(nums,low,high):
    if(low<high):
        s = partition(nums,low,high)
        quick_sort(nums,low,s-1)
        quick_sort(nums,s+1,high)

    

nums = [7,4,10,1,6]
quick_sort(nums,0,4)
print(nums)

#TIME COMPLEXITY:
# worst case = o(n**2)
# best and avg case = o(nlogn)
# SPACE COMPLEXITY:O(1)
