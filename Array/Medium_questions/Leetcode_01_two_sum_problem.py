nums = [1,2,3,4,5,6]
target = 12
n - len(nums)

dict = {}
for i in range(0, n):
    remaining = target - nums[i]
    if remaining in dict:
        return dict[remaining, i]
    
    dict[nums[i]] = i