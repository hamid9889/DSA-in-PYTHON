nums = [1,0,2,4,3,0,0,3,5,1]
n =  len(nums)
dict = []

for i in range(0 , n):
    if nums[i] != 0:
        dict.append(nums[i])  
    
nz = len(dict)
for i in range(0 ,nz):
    nums[i] = dict[i]   

for i  in range(nz , n):
    nums[i] = 0         


"""
time and space complexity is O(N)
and the soace complexity is o(1)
"""