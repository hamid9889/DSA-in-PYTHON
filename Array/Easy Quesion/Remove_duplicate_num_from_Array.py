nums= [1,1,3,3,4,6,7,8 ,8,9]

n = len(nums)
map = {}
for i in range(0 , n):
    map[nums[i]] = 0
    
j = 0
for k in map:
    nums[j] = k
    j +=1

return j   

'''
time complexity of this in brout forcr case is o(2N) ~~ O (N)
space complexity is o(N)
'''
#optimal  solution 

 