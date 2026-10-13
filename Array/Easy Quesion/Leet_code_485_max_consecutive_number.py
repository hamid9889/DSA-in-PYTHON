nums = [1,1,1,1,0,0,1,1,1]

count = 0
max_count = 0

for i in nums:
    if i ==1:
        count +=1
    maximun = max(max_count, count)
    
    else : 
        count = 0
        
return maximun        
        
        
        """
        time complexity is o(N )
        space complexity is o(n)
        
        """