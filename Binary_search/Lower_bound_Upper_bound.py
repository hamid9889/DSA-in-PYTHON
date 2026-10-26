# code for lower or upper bounf
nums = []
n = len(nums)
lb = n
low = 0
high = n-1
while low <=high:
    mid = (low + high) //2
    if nums[mid]==target :
        lb = mid
        high = mid-1
    else:
        low -=1    
return lb

"""
the time complexity is O(log_base2 N)
space complexity is o(1)

"""
# code for lower or upper bounf
    
    
nums = []
n = len(nums)
ub = n
low = 0
high = n-1
while low <=high:
    mid = (low + high) //2
    if nums[mid]>=target :
        lb = mid
        high = mid-1
    else:
        low -=1    
return ub   
       
"""
the time complexity is O(log_base2 N)
space complexity is o(1)

"""