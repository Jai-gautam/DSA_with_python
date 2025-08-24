# MERGE SORT : 

def merge_arr(left,right):
    n = len(left)
    m = len(right)
    result = []
    i = 0
    j =0
    while(i<n and j<m):
        if (left[i]<=right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j+=1

    while(i<n):
        result.append(left[i])
        i+=1

    while(j<m):
        result.append(right[j])
        j+=1

    return result
    
def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_half = merge_sort(left_arr)
    right_half = merge_sort(right_arr)

    return merge_arr(left_half,right_half)
    
arr = [7,5,4,33,444,55,7,2,1,3,6]
ans = merge_sort(arr)
print(ans)