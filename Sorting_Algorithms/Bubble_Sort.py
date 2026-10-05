# bubble sort  [ adjeacent swap ]
nums = [9,8,7,6,5,4,3,2,1]
def bubble(nums):
    n = len(nums)
    

    for i in range(n -2, -1 , -1):
                for j in range(0 , i+1):
                    if nums[j] >  nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                  
    return nums

        
# time and Space   o(n (n +1 )/2) ~~ o (N 2),,  space o(1)  for avg or wrost case

              