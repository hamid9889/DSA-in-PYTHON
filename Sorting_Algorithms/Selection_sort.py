#selection sort
nums = [9,8,7,9,1,1,3,2,1,0]

def selection_sort(nums):
    n = len(nums)
    for i in range(0 ,n):
        mini_index=i 
        for j in range(i+1, n):
            if nums[j]<nums[mini_index]:
                mini_index=j
                
            nums[i], nums[mini_index] = nums[mini_index] ,nums[i]
    return nums



a = selection_sort(nums)
print(a)


# time complexity is 0(N(n+1/2)) ~~ o(n`2`)  space complexity 0(1)

a = [1,3,4,5,6,7,8,9]

def sort(a):
    n = len(a)
    for i in range(0 , n):
        max_ind = i
        
        for j in  range(i+1 , n):
            if a[j]>a[max_ind]:
              max_ind = j
            
            a[i],a[max_ind] =a[max_ind], a[i]
        
    return a

# time complexity is 0(N(n+1/2)) ~~ o(n`2`)  space complexity 0(1)