nums = [1,2,3,4,5,5,7,6,11,342]

n = len(nums)
my_set = set()
for i in range(0 , n):
    my_set.add(nums[i])
    
longest = 0
for num in my_set:
    if num-1 not in my_set:
        x =  num
        count = 1
        while   x+1 in my_set:
            count +=1
            num +=1
            longest = max(longest , count)

return longest             

"""
the tme and space complexity id O(3N) ~~O(N)
spce complexity it o(N)
"""
