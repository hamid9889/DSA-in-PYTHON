nums = [-2,1,-3,4,-1,2,1,-5,4]

maxi = nums[0]
total = 0
for i in nums:
    total = total + nums[i]
    maxi = max(maxi , total)
    
    if total <0:
        total = 0
    return maxi 


"""
time  complexity is O (N)
and space complexity is O(1)
"""
    