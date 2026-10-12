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

# optimal solution 


nums = [1,0,2,4,3,0,0,3,5,1]
n =  len(nums)

if len(nums) ==0:
    return

i = 0
while i < n :
    if nums[i] != 0:
        break
    i +=1

if i == len(nums):
    return

j = i+1
while j <n:
    if nums[j] == 0:
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
j +=1            


"""
time complexity is o(N) 'a

and space complexity is the o (1)
"""
