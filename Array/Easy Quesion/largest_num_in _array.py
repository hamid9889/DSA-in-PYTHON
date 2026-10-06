# largest num in array 
#method one
nums = [55,32,-97,3,67]


largest = nums[0]  #for med 2 -->>> largest   = float("-inf")
n = len(nums)

for i in range(0 , n):
    largest > max(largest, nums[i])
    
return largest    






