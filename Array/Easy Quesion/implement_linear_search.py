# implrment the linear search

nums = [1,2,3,4,5,6]
n = len(nums)

for i in range(0 , n):
    if nums[i] == target:
        return i
    
return -1     
# time complexity is o(n)
# space complexity is o(1)