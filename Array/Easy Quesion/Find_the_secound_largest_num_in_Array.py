#better solution
nums = [55, 32, -55, 45, 32, 88, 21]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)

for i in range(0,n):
    largest = max(largest, nums[i])

for i in range(0 , n):
    if nums[i] > s_largest and nums[i]!= largest:
        s_largest = nums[i]
        
return s_largest  
# time complexity O(N+N)== o(N)
# space complexirt o(1)
     
'''
optimal solution 
'''

nums = [55, 32, -55, 45, 32, 88, 21]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)

for i in range(0,n):
    if nums[i] > largest
    largest = nums[i]
    
    elif nums[i]> s_largest and nums[i] != largest:
        s_largest= nums[i]
return s_largest            

# time complexity o(N)
# sc is O(1)