nums= [1,2,3,4,2,3,4,5,6,7,8,5,6,7,8,9,5,89]
n = len(nums)
hash_map = {}
for i in range(0,n):

    hash_map[nums[i]] = hash_map.get(nums[i],0)+1

print(hash_map)

