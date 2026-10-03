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
