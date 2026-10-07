# merge dort work on divide and merge

#merge two sorted array 
left = [1,2,3,4]
right = [1,1,3,4,5,6,7]

def merg_arrray(left, right):
    result = []
    i , j = 0, 0
    n , m = len(left), len(right)
    
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    if i< n :
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j +=1


    return result    
         
              

                
                
# main merge sort working

nums = [2,3,4,3,1,5,5,4,6] # n= 9
                

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_arr = nums[ : mid]
    right_arr = nums[mid : ]
    
    left = merge_sort(left_arr)  # recursion for main left
    left = merge_sort(left_arr)  # recursion for main right
    right = merge_sort(right_arr)
    return merg_arrray(left , right) # upper sorted function call


""" 
Time and space complexity of this o(log2 N x N) == o(NlogN)

space complexity is o(N)
"""





















