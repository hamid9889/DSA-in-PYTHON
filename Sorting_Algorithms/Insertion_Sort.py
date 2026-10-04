nums = [9,8,7,6,5,4,3,2,1]
def func(num):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j >=0 and nums[j]> key:
            nums[j+1] = nums[j]
            
        nums[j+1] = key
    # here all solution 
 
  
#time complexity o(N^2)
# space complexity o(1)        