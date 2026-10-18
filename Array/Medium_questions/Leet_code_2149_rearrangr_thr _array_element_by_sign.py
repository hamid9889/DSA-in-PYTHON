nums = [2,3,-7,4,-9,-4]

n = len(nums)
result = [0]*n
pos_index , neg_index = 0 , 1

for i in range(0, n):
    if nums[i] >= 0:
        result[pos_index] = nums[i]
        pos_index =+2
    else:
        result[neg_index] = nums[i]
        neg_index +=2
return result            



"""
time complexity iis O(N)
ans the space complexity os O(1)  or O(N)
"""
