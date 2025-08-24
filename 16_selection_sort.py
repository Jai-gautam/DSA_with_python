# SELECTION SORT : first element ko i lete h and usko minimum man lete h
#                : fir uske next ko j lete h or usko iterate karte h, if j<min , swap karte h
#                : i ko iterate karte h again uper vala process karte h

nums =[5,3,6,8,1,2,100]

def selection_sort_ascending(nums):
    n = len(nums)
    for i in range (0,n-1):
        min_item = i
        for j in range(i+1,n):
            if(nums[j]<nums[min_item]):
                min_item = j                                # changing index of min_item
        nums[i],nums[min_item] = nums[min_item],nums[i]     # swapping
        


    print(nums)

selection_sort_ascending(nums)


def selection_sort_descending(nums):
    n = len(nums)
    for i in range (0,n-1):
        max_item = i
        for j in range(i+1,n):
            if(nums[j]>nums[max_item]):
                max_item = j                                # changing index of max_item

        nums[max_item],nums[i] = nums[i],nums[max_item]      # swapping
                

    print(nums)

selection_sort_descending(nums)