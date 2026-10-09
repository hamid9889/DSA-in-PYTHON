nums = [3,9,6,6,3,2,6,8]
n = len(nums)
k = n %k
def reverse(nums , left , right):
    while left < right:
        nums[left], nums[right] = nums[right] , nums[left]
        
        
        left +=1 
        right+=1

reverse(n-k, n-1)        
reverse(0,n-k-1)        
reverse(0, n-1)

# time and space complexity